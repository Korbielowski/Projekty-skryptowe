from kivy.lang import Builder

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

        MDBottomNavigationItem:
            name: "Income"
            text: "Income"
            icon: "cash-100"
            # MDFillRoundFlatButton:
            #     text: "cofnij"
            #     pos_hint: {"center_x": 0.5,"center_y": 0.5}
            #     on_release: app.root.current = "main"
"""


class MainScreen(MDScreen):
    pass


class SecondScreen(MDScreen):
    pass


class WindowManager(ScreenManager):
    pass


class Budget_for_dummies(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


if __name__ == "__main__":
    Budget_for_dummies().run()
