from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager


class FirstScreen(Screen):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error'


class Screen_Manager(ScreenManager):
    pass


kv = Builder.load_file('application.kv')


class Calculator(App):
    def build(self):
        return kv


if __name__ == '__main__':
    Calculator().run()


