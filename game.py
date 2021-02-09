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
        self.scr.addch(1, 1, self.key)
