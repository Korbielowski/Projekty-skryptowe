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
    name: 'main'
    MDBottomNavigation:
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'home'
            text: 'home'
            icon: 'home'

            MDLabel:
                text: "There is nothing here"
                halign: "center"
                valign: "center"
                theme_text_color: "Custom"
                text_color: "grey"
            MDFloatingActionButton:
                icon: "plus"
                pos_hint: {'center_x': 0.95,'center_y': 0.075}

        MDBottomNavigationItem:
            name: 'stats'
            text: 'stats'
            icon: "chart-bar"

        MDBottomNavigationItem:
            name: 'more'
            text: 'more'
            icon: "dots-horizontal"

            AnchorLayout:
                anchor_x: "right"
                anchor_y: "top"
                MDRectangleFlatIconButton:
                    icon: "cog"
                    text: "Settings"

            AnchorLayout:
                anchor_x: "center"
                anchor_y: "top"
                MDRectangleFlatIconButton:
                    icon: "information"
                    text: "Info"

            AnchorLayout:
                anchor_x: "left"
                anchor_y: "top"
                MDRectangleFlatIconButton:
                    icon: "palette"
                    text: "App Theme"

<SecondScreen>:
    name: 'second'
    GridLayout:
        cols: 2
        MDFillRoundFlatButton:
            text: "cofnij"
            md_bg_color: [0, 0, 1, 1]
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            on_release: app.root.current = 'main'
"""


class MainScreen(MDScreen):
    pass


class SecondScreen(MDScreen):
    pass


class WindowManager(ScreenManager):
    pass


class Budget_for_dummies(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def wysun(self):
        bottom = MDListBottomSheet()
        for i in range(1, 11):
            bottom.add_item(f"Standart Item {i}", lambda x, y=MainScreen(): y.zmien())
        bottom.open()


if __name__ == "__main__":
    Budget_for_dummies().run()
