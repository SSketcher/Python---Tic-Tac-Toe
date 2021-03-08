import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

#Seting window fixed dimensions
Window.size = (400, 440)

#Loading kivy language file
Builder.load_file('game.kv')

class TicTacTou(Widget):
    def put_sumbol(self):
        pass

    def check(self):
        pass

    

class Game(App):
    def build(self):
        return TicTacTou()

if __name__ == '__main__':
    Game().run()