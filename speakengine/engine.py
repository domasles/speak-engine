from typing import TYPE_CHECKING
from kivy.clock import Clock

if TYPE_CHECKING:
    from scene import GameScene

class GameEngine:
    def __init__(self, desired_fps: int=60):
        self.current_scene = None
        self.desired_fps = desired_fps

    def run(self):
        Clock.schedule_interval(self.update, 1 / self.desired_fps)

    def update(self, dt: float):
        if self.current_scene:
            self.current_scene.update(dt)
            self.current_scene.render()

    def set_scene(self, scene: "GameScene"):
        self.current_scene = scene
