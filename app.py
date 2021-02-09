import curses as c
from game import Game

class App():

    def init(self, scrn):
        self.scr = scrn
        c.noecho()
        c.cbreak()
        self.game = Game(self.scr)
        self.game.main()
    
    def get_screen(self):
        return self.scr


if __name__ == "__main__":
    app = App()
    c.wrapper(app.init)
    
