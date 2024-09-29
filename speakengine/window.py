from kivy.uix.widget import Widget
from kivy.core.window import Window

red = 0
green = 0
blue = 0
alpha = 0

class GameWindow(Widget):
    def __init__(self, title: str="Speak Engine", width: int=800, height: int=600, bg_color: tuple=(red, green, blue, alpha)):
        super().__init__()

        Window.size = (width, height)
        Window.title = title
        Window.clearcolor = bg_color

    def set_fullscreen(self, fullscreen: bool=True):
        Window.fullscreen = "auto" if fullscreen else False

    def set_bg_color(self, color: tuple=(red, green, blue, alpha)):
        Window.clearcolor = color
