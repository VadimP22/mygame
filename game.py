from menu import Menu
import sys
import threading
import time

class Game():
    
    def check_key(self):
        #import sys
        while True:
            #self.key = ''
            self.key = self.scr.getkey()
            time.sleep(0.0000000000000000000000001)
            self.key = ''
            time.sleep(0.0000000000000000000000001)



    def __init__(self, scrn):
        self.scr = scrn
        self.key = ''

        listener = threading.Thread(target=self.check_key)
        listener.setDaemon(True)
        listener.start()

    def main(self):
        menu = Menu(3, 0, ['Zero', 'One', 'Two', 'Exit'])

        def exit():
            sys.exit(0)
            
        menu.set_onclick("Exit", exit)


        while True:
            #self.key = ''
            #self.scr.refresh()
            #self.check_key()
            
            menu.process(self.key)
            
            
            menu.draw(self.scr)
            #menu.process(self.key)
            self.scr.refresh()

    # def mainloop(self):
    #     menu = Menu(3, 0, 'absolutely', 'b', 'cee')
    #     menu.draw(self.scr)
    #     menu.process(self.key)
