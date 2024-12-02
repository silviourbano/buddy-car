import kivy
from kivy.app import App
from kivy.uix.button import Button
import os

os.environ["KIVY_GL_BACKEND"] = "sdl2"

kivy.logger.Logger.setLevel('DEBUG')

class TestApp(App):
    def build(self):
        return Button(text="Hello, Kivy!")

if __name__ == '__main__':
    TestApp().run()
