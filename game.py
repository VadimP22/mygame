from menu import Menu
import sys

class Game():
    
    def __init__(self, scrn):
        self.scr = scrn
        self.key = ''

    def main(self):
        menu = Menu(3, 0, ['One', 'Two', 'Exit'])

        def exit():
            sys.exit(0)
        menu.labels[2].set_onclick(exit)
        
        while True:
            #self.scr.refresh()
            self.key = self.scr.getkey()
           
            menu.process(self.key)
            menu.draw(self.scr)
            #menu.process(self.key)
            self.scr.refresh()

    # def mainloop(self):
    #     menu = Menu(3, 0, 'absolutely', 'b', 'cee')
    #     menu.draw(self.scr)
    #     menu.process(self.key)
