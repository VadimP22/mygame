class MenuLabel():
    def __init__(self, y, x, name):
        self.name = name
        self.selected = False 
        self.y = y
        self.x = x

        def default_onclick():
            pass

        self.onclick = default_onclick

    def set_onclick(self, func):
        self.onclick = func

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False
    



class Menu():
    def __init__(self, y, x, *names):
        self.selector = 0
        self.active = True
        self.labels = []
        self.x = x
        self.y = y
        self.names = names
        #find max len
        max_len = 0
        for name in names:
            if len(name) > max_len:
                max_len = len(name)
        
        for n in range(len(self.names)):
            self.labels.append(MenuLabel(self.y + n, int(self.x + abs(len(self.names[n]) - max_len)/2) + 1, self.names[n]))

        if self.active:
            self.labels[self.selector].select()


    def draw(self, scr):
        #self.labels[2].select()
        for label in self.labels:
            if label.selected:
                scr.addch(label.y, label.x - 1, '[')
                scr.addch(label.y, label.x + len(label.name), ']')
            scr.addstr(label.y, label.x, str(label.name))

    def process(self, scr):
       self.labels[2].select()

