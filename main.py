
from kivy.app import App
from kivy.uix.label import Label

class RahmanApp(App):
    def build(self):
        return Label(text='رحمان رحمتی', font_size=32)

RahmanApp().run()
