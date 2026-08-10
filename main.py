
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase

LabelBase.register(name="Vazir", fn_regular="Vazirmatn-Regular (1).ttf")

class RahmanApp(App):
    def build(self):
        return Label(text='رحمان رحمتی', font_size=32, font_name="Vazir")

RahmanApp().run()
