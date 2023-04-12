from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.screenmanager import ScreenManager


KV = """
WindowManager:
    MainScreen:
    SecondScreen:

<MainScreen>:
    name: "main"

    MDBottomNavigation:
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: "home"
            text: "home"
            icon: "home"

            MDLabel:
                text: "There is nothing here"
                halign: "center"
                valign: "center"
                theme_text_color: "Custom"
                text_color: "grey"

            MDFloatingActionButton:
                icon: "plus"
                pos_hint: {"center_x": 0.95,"center_y": 0.075}
                icon_color: "grey"
                md_bg_color: "white"
                on_release: app.root.current = "second"

        MDBottomNavigationItem:
            name: "stats"
            text: "stats"
            icon: "chart-bar"

        MDBottomNavigationItem:
            name: "more"
            text: "more"
            icon: "dots-horizontal"

            StackLayout:
                MDRectangleFlatIconButton:
                    icon: "cog"
                    text: "Settings"
                    size_hint: 0.3333, 0.3333
                    theme_text_color: "Custom"
                    line_color: "grey"
                    text_color: "grey"
                    icon_color: "grey"

                MDRectangleFlatIconButton:
                    icon: "information"
                    text: "Info"
                    size_hint: 0.3333, 0.3333
                    theme_text_color: "Custom"
                    line_color: "grey"
                    text_color: "grey"
                    icon_color: "grey"

                MDRectangleFlatIconButton:
                    icon: "palette"
                    text: "App Theme"
                    size_hint: 0.3333, 0.3333
                    theme_text_color: "Custom"
                    line_color: "grey"
                    text_color: "grey"
                    icon_color: "grey"

<SecondScreen>:
    name: "second"

    MDBottomNavigation:
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: "Spendings"
            text: "Spendings"
            icon: "cash"
            
            BoxLayout:
                orientation: 'vertical'

                MDTextField:
                    id: amount
                    helper_text: "Enter amount"
                    helper_text_mode: "on_error"
                    icon_right: "currency-eur"
                    multiline: False
                    size_hint: 0.2, 0.1
                    pos_hint: {'center_x': 0.5,'center_y': 0.1}

                StackLayout:
                    MDRectangleFlatIconButton:
                        icon: "train-car"
                        text: "Transportation"
                        size_hint: 0.3333, 0.3333

                    MDRectangleFlatIconButton:
                        icon: "lightning-bolt"
                        text: "Electricity"
                        size_hint: 0.3333, 0.3333

                    MDRectangleFlatIconButton:
                        icon: "cart"
                        text: "Groceries"
                        size_hint: 0.3333, 0.3333
                    
                    MDRectangleFlatIconButton:
                        icon: "theater"
                        text: "Entertainment"
                        size_hint: 0.3333, 0.3333

                MDFillRoundFlatButton:
                    text: "Add spending"
                    pos_hint: {"center_x": 0.5,"center_y": 0.5}
                    on_release: 
                        app.root.current = "main"
                        app.add_spending(amount.text)

        MDBottomNavigationItem:
            name: "Income"
            text: "Income"
            icon: "cash-100"
"""


class MainScreen(MDScreen):
    pass


class SecondScreen(MDScreen):
    pass


class WindowManager(ScreenManager):
    pass


class Budget_for_dummies(MDApp):
    def build(self):
        Window.top = 100
        Window.right = 100
        Window.size = (450, 700)
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def add_spending(self, amount):
        if isinstance(amount, float):
            print("pieniądze")
        else:
            print("błąd")


if __name__ == "__main__":
    Budget_for_dummies().run()
