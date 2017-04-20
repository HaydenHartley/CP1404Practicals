from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class StringToLabel(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.string_list = ["word", "words", "more words", "another word", "even more words"]

    def build(self):
        self.title = "List of Strings"
        self.root = Builder.load_file('strToLabel.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for string in self.string_list:
            temp_label = Label(text=string)
            self.root.ids.stringList.add_widget(temp_label)


StringToLabel().run()
