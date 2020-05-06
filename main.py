import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
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

    def start(self):

        pass

sm = Builder.load_file("bm.kv")

class BMApp(App):


    def __init__(self, **kwargs):
        super(BMApp, self).__init__(**kwargs)
        self.hang  = NumericProperty(0)
        self.rest  = NumericProperty(0)
        self.rest_after_hangs = NumericProperty(0)
        self.rest_after_sets = NumericProperty(0)

    def build(self):
        #self.start()
        print(self.root.ids.train_screen.ids.hang.ids.anim_lab.text)
        self.update_total()
        return sm

    def update_total(self):
        tmp_cons_hangs = (int(self.root.ids.start_screen.ids.hang_time.ids.adj_el.ids.element_value.text) + int(self.root.ids.start_screen.ids.rest_time.ids.adj_el.ids.element_value.text))* int(self.root.ids.start_screen.ids.cons_hangs.ids.adj_el.ids.element_value.text)
        tmp_cons_hangs_rest = tmp_cons_hangs + int(self.root.ids.start_screen.ids.rest_after_hangs.ids.adj_el.ids.element_value.text)
        tmp_set_time = tmp_cons_hangs_rest * int(self.root.ids.start_screen.ids.hang_rounds.ids.adj_el.ids.element_value.text) + int(self.root.ids.start_screen.ids.rest_after_set.ids.adj_el.ids.element_value.text)
        t_total = tmp_set_time * int(self.root.ids.start_screen.ids.n_sets.ids.adj_el.ids.element_value.text)
        print( f"{(t_total//60):02d}:{(t_total%60):02d}")
        self.root.ids.start_screen.ids.total_time.text = f"{(t_total//60):02d}:{(t_total%60):02d}"
        self.hang  = int(self.root.ids.start_screen.ids.hang_time.ids.adj_el.ids.element_value.text)
        self.rest  = int(self.root.ids.start_screen.ids.rest_time.ids.adj_el.ids.element_value.text)
        self.rest_after_hangs = int(self.root.ids.start_screen.ids.rest_after_hangs.ids.adj_el.ids.element_value.text)
        self.rest_after_sets = int(self.root.ids.start_screen.ids.rest_after_set.ids.adj_el.ids.element_value.text)

    def pause(self):
        pass
    #
    # def increment_time(self, interval):
    #     print(f"{(self.number//60):02d}:{(self.number%60):02d}")
    #
    #     self.root.ids.train_screen.ids.hang.ids.anim_lab.text = f"{(self.number//60):02d}:{(self.number%60):02d}"
    #     self.number += 1

    def countdown_hang(self, interval):
        self.root.ids.train_screen.ids.hang.ids.anim_lab.text = f"{(self.tmp_count//60):02d}:{(self.tmp_count%60):02d}"
        self.tmp_count -= 1
        if self.tmp_count==-1:
            return

    def countdown_pause(self, interval):
        self.root.ids.train_screen.ids.pause.ids.anim_lab.text = f"{(self.tmp_count//60):02d}:{(self.tmp_count%60):02d}"
        self.tmp_count -= 1
        if self.tmp_count==-1:
            return


    def countdown_rest(self, interval):
        print(self.tmp_count)
        self.root.ids.train_screen.ids.rest.ids.anim_lab.text = f"{(self.tmp_count//60):02d}:{(self.tmp_count%60):02d}"
        self.tmp_count -= 1
        if self.tmp_count==-1:
            return
    def wait(self, interval):
        print("waiting")

    def start(self):
        for set in list(range(int(self.root.ids.start_screen.ids.n_sets.ids.adj_el.ids.element_value.text))):
            for hang_round in list(range(int(self.root.ids.start_screen.ids.hang_rounds.ids.adj_el.ids.element_value.text))):
                for chang in list(range(int(self.root.ids.start_screen.ids.cons_hangs.ids.adj_el.ids.element_value.text))):
                    self.tmp_count = self.hang
                    Clock.unschedule(self.countdown_hang)
                    Clock.schedule_interval(self.countdown_hang, 1)

                    self.tmp_count = self.rest
                    #
                    Clock.schedule_interval(self.countdown_rest, 1)
                    Clock.unschedule(self.countdown_rest)
                self.tmp_count = self.rest_after_hangs
                #
                Clock.schedule_interval(self.countdown_pause, 1)
                Clock.unschedule(self.countdown_pause)
            self.tmp_count = self.rest_after_sets

            Clock.schedule_interval(self.countdown_pause, 1)
            Clock.unschedule(self.countdown_pause)

if __name__ == '__main__':
    BMApp().run()
