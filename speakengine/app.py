from typing import Callable
from kivy.app import App

class GameApp(App):
    def __init__(self, app: Callable[[], None]):
        super().__init__()
        self.app = app
    
    def build(self):
        return self.app()
