import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class Budget_for_dummies(App):
    def build(self):
        Button(text="opcje", font_size="14", background_color=(1, 1, 1, 1))
        return Label(text="Budget for Dummies")


if __name__ == "__main__":
    Budget_for_dummies().run()
