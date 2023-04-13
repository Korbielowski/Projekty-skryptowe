from kivy.lang import Builder
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

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
    SettingsScreen:
    InfoScreen:

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
                pos_hint: {"center_x": 0.915,"center_y": 0.06}
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
                    on_release: app.root.current = "settings_screen"

                MDRectangleFlatIconButton:
                    icon: "information"
                    text: "Info"
                    size_hint: 0.3333, 0.3333
                    theme_text_color: "Custom"
                    line_color: "grey"
                    text_color: "grey"
                    icon_color: "grey"
                    on_release: app.root.current = "info_screen"

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
                    id: amount_spending
                    helper_text: "Enter amount"
                    helper_text_mode: "on_error"
                    icon_right: "currency-eur"
                    multiline: False
                    required: True
                    size_hint: 0.2, 0.1
                    pos_hint: {'center_x': 0.5,'center_y': 0.1}

                StackLayout:
                    id: chip_box

                    MDChip:
                        id: transportation
                        icon_right: "train-car"
                        text: "Transportation"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                    MDChip:
                        id: electricity
                        icon_right: "lightning-bolt"
                        text: "Electricity"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                    MDChip:
                        id: groceries
                        icon_right: "cart"
                        text: "Groceries"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                    MDChip:
                        id: entertainment
                        icon_right: "theater"
                        text: "Entertainment"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                    MDChip:
                        id: clothes
                        icon_right: "tshirt-crew-outline"
                        text: "Clothes"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                    MDChip:
                        id: gift
                        icon_right: "gift-outline"
                        text: "Gift"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                MDFillRoundFlatButton:
                    text: "Add spending"
                    pos_hint: {"center_x": 0.5,"center_y": 0.5}
                    on_release: 
                        app.root.current = "main"
                        root.add_spending(amount_spending.text, chip_box.children)
                        amount_spending.text=""

        MDBottomNavigationItem:
            name: "Income"
            text: "Income"
            icon: "cash-100"

            BoxLayout:
                orientation: 'vertical'

                MDTextField:
                    id: amount_income
                    helper_text: "Enter amount"
                    helper_text_mode: "on_error"
                    icon_right: "currency-eur"
                    multiline: False
                    required: True
                    size_hint: 0.2, 0.1
                    pos_hint: {'center_x': 0.5,'center_y': 0.1}

                StackLayout:
                    id: chip_box

                    MDChip:
                        id: salary
                        icon_right: "briefcase-outline"
                        text: "Salary"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                    MDChip:
                        id: intrest
                        icon_right: "piggy-bank-outline"
                        text: "Intrest"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                    MDChip:
                        id: gift
                        icon_right: "gift-outline"
                        text: "Gift"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self)

                MDFillRoundFlatButton:
                    text: "Add income"
                    pos_hint: {"center_x": 0.5,"center_y": 0.5}
                    on_release: 
                        app.root.current = "main"
                        root.add_income(amount_income.text, chip_box.children)
                        amount_income.text=""

<SettingsScreen>:
    name: "settings_screen"

    MDLabel:
        text: "Tutaj będą opcje"

<InfoScreen>:
    name: "info_screen"

    MDLabel:
        text: "Tutaj będą informacje o aplikacji"
"""


class MainScreen(MDScreen):
    pass


class SecondScreen(MDScreen):
    def remove_marks(self, selected_chip):
        for chip in self.ids["chip_box"].children:
            if chip != selected_chip:
                chip.active = False

    def add_spending(self, amount_sent, chips):
        # print(chips)
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            for chip in chips:
                if chip.active:
                    self.stored_spending = JsonStore("spending_data.json")
                    if self.stored_spending.exists(chip.text):
                        am = self.stored_spending.get(chip.text)["amount"]
                        self.stored_spending.put(chip.text, amount=self.amount + am)
                        # print("Zaktualizowano")
                    else:
                        self.stored_spending.put(chip.text, amount=self.amount)
                        # print("Stworzono")

    def add_income(self, amount_sent, chips):
        # print(chips)
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            for chip in chips:
                if chip.active:
                    self.stored_spending = JsonStore("income_data.json")
                    if self.stored_spending.exists(chip.text):
                        am = self.stored_spending.get(chip.text)["amount"]
                        self.stored_spending.put(chip.text, amount=self.amount + am)
                        # print("Zaktualizowano")
                    else:
                        self.stored_spending.put(chip.text, amount=self.amount)
                        # print("Stworzono")


class SettingsScreen(MDScreen):
    pass


class InfoScreen(MDScreen):
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


if __name__ == "__main__":
    Budget_for_dummies().run()
