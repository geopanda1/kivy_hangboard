import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.core.image import Image
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)

class RoundButton(Button):

    def __init__(self, **kwargs):
        super(RoundButton, self).__init__(**kwargs)

class AdjustElement(BoxLayout):

    def __init__(self, **kwargs):
        super(AdjustElement, self).__init__(**kwargs)

    def minus(self):
        self.ids.element_value.text = str(int(self.ids.element_value.text) - 1)

    def plus(self):
        self.ids.element_value.text = str(int(self.ids.element_value.text) + 1)

class AdjustBar(GridLayout):

    def __init__(self, **kwargs):
        super(AdjustBar, self).__init__(**kwargs)



class StartScreen(Screen):
    pass

class TrainScreen(Screen):
    pass

sm = Builder.load_file("bm.kv")

class BMApp(App):

    def build(self):
        self.update_total()
        return sm

    # def update_total(self):
    #     pass

    def update_total(self):
        tmp_cons_hangs = (int(self.root.ids.start_screen.ids.hang_time.ids.adj_el.ids.element_value.text) + int(self.root.ids.start_screen.ids.rest_time.ids.adj_el.ids.element_value.text))* int(self.root.ids.start_screen.ids.cons_hangs.ids.adj_el.ids.element_value.text)
        tmp_cons_hangs_rest = tmp_cons_hangs + int(self.root.ids.start_screen.ids.rest_after_hangs.ids.adj_el.ids.element_value.text)
        tmp_set_time = tmp_cons_hangs_rest * int(self.root.ids.start_screen.ids.hang_rounds.ids.adj_el.ids.element_value.text) + int(self.root.ids.start_screen.ids.rest_after_set.ids.adj_el.ids.element_value.text)
        t_total = tmp_set_time * int(self.root.ids.start_screen.ids.n_sets.ids.adj_el.ids.element_value.text)
        print( f"{(t_total//60):02d}:{(t_total%60):02d}" )
        self.root.ids.start_screen.ids.total_time.text = f"{(t_total//60):02d}:{(t_total%60):02d}"

if __name__ == '__main__':
    BMApp().run()
