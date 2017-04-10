from kivy.app import App
from kivy.lang import Builder


class MetresToKilometres(App):
    def build(self):
        self.title = "Metres To Kilometres"
        self.root = Builder.load_file('metresToKilometres.kv')
        return self.root

MetresToKilometres().run()