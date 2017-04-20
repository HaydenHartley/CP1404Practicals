from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KILOMETRES = 1.60934


class MilesToKilometres(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Miles To Kilometres"
        self.root = Builder.load_file('milesToKilometres.kv')
        return self.root

    def handle_calculate_km(self):
        kilometres = self.get_valid_number() * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(kilometres)

    def handle_count(self, difference):
        self.root.ids.miles_input.text = str(self.get_valid_number() + difference)

    def get_valid_number(self):
        try:
            valid_num = float(self.root.ids.miles_input.text)
            return valid_num
        except ValueError:
            return 0


MilesToKilometres().run()
