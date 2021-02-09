from menu import Menu

class Game():
    
    def __init__(self, scrn):
        self.scr = scrn
        self.key = ''

    def main(self):
        while True:
            self.key = self.scr.getkey()
            self.mainloop()
            self.scr.refresh()

    def mainloop(self):
        menu = Menu(3, 0, 'absolutely', 'b', 'cee')
        menu.draw(self.scr)
        menu.process(self.key)
