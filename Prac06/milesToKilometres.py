from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometres(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Miles To Kilometres"
        self.root = Builder.load_file('milesToKilometres.kv')
        return self.root


MilesToKilometres().run()
