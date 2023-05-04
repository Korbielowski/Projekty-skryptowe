import json
import os.path

from matplotlib import pyplot as plt

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.screenmanager import ScreenManager

KV = """
WindowManager:
    MainScreen:
    SecondScreen:
    CustomSpending:
    CustomIncome:
    SettingsScreen:
    InfoScreen:
    AppThemeScreen:

<MainScreen>:
    name: "main"

    MDBottomNavigation:
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            id: "home"
            name: "home"
            text: "home"
            icon: "home"
            # on_tab_release: root.print_data()

            # GridLayout:
            #     cols: 1
            on_enter: 
                root.load_income_spending()

            MDBoxLayout:
                id: card_layout
                orientation: 'vertical'

            # MDLabel:
            #     text: "Main menu"
            #     halign: "center"
            #     valign: "center"
            #     theme_text_color: "Custom"
            #     text_color: "grey"

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
            on_enter:
                root.load_chart()

            BoxLayout:
                id: box
                size_hint_y: .8
                pos_hint: {"top":1}

            MDLabel:
                text: "Charts and stats"
                halign: "center"
                valign: "center"
                theme_text_color: "Custom"
                text_color: "grey"

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
                    on_release: app.root.current = "app_theme_screen"

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
                    size_hint: 0.3, 0.2
                    pos_hint: {'center_x': 0.5,'center_y': 0.2}

                StackLayout:
                    id: spending_box

                    MDChip:
                        id: transportation
                        icon_right: "train-car"
                        text: "Transportation"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "spending_box")

                    MDChip:
                        id: electricity
                        icon_right: "lightning-bolt"
                        text: "Electricity"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "spending_box")

                    MDChip:
                        id: groceries
                        icon_right: "cart"
                        text: "Groceries"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "spending_box")

                    MDChip:
                        id: entertainment
                        icon_right: "theater"
                        text: "Entertainment"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "spending_box")

                    MDChip:
                        id: clothes
                        icon_right: "tshirt-crew-outline"
                        text: "Clothes"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "spending_box")

                    MDChip:
                        id: gift
                        icon_right: "gift-outline"
                        text: "Gift"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "spending_box")

                    MDChip:
                        id: user
                        icon_right: "plus"
                        text: "Custom"
                        size_hint: 0.3333, 0.3333
                        # on_active: if self.active: 
                        on_press:
                            root.remove_marks(self, "spending_box")
                            app.root.current = "custom_spending"

                MDFillRoundFlatButton:
                    text: "Add spending"
                    md_bg_color: "grey"
                    pos_hint: {"center_x": 0.5,"center_y": 0.8}
                    on_release: 
                        app.root.current = "main"
                        root.add_income_or_spending(amount_spending.text, spending_box.children, "spending_box")
                        amount_spending.text=""

                MDFillRoundFlatButton:
                    text: "Back"
                    md_bg_color: "grey"
                    pos_hint: {"center_x": 0.5,"center_y": 0.2}
                    on_release: 
                        app.root.current = "main"
                        root.remove_marks(self, "spending_box")

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
                    size_hint: 0.3, 0.2
                    pos_hint: {'center_x': 0.5,'center_y': 0.2}

                StackLayout:
                    id: income_box

                    MDChip:
                        id: salary
                        icon_right: "briefcase-outline"
                        text: "Salary"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "income_box")

                    MDChip:
                        id: intrest
                        icon_right: "piggy-bank-outline"
                        text: "Intrest"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "income_box")

                    MDChip:
                        id: gift
                        icon_right: "gift-outline"
                        text: "Gift"
                        size_hint: 0.3333, 0.3333
                        on_active: if self.active: root.remove_marks(self, "income_box")

                    MDChip:
                        id: user
                        icon_right: "plus"
                        text: "Custom"
                        size_hint: 0.3333, 0.3333
                        # on_active: if self.active: 
                        on_press:
                            root.remove_marks(self, "income_box")
                            app.root.current = "custom_income"

                MDFillRoundFlatButton:
                    text: "Add income"
                    md_bg_color: "grey"
                    pos_hint: {"center_x": 0.5,"center_y": 0.5}
                    on_release: 
                        app.root.current = "main"
                        root.add_income_or_spending(amount_income.text, income_box.children, "income_box")
                        amount_income.text=""

                MDFillRoundFlatButton:
                    text: "Back"
                    md_bg_color: "grey"
                    pos_hint: {"center_x": 0.5,"center_y": 0.2}
                    on_release: 
                        app.root.current = "main"
                        root.remove_marks(self, "income_box")
<CustomSpending>:
    name: "custom_spending"

    GridLayout:
        rows: 4
        
        MDLabel:
            text: "Add custom spending"

        MDTextField:
            id: name_spending
            helper_text: "Enter name"
            helper_text_mode: "on_error"
            multiline: False
            required: True

        MDTextField:
            id: amount_custom_spending
            helper_text: "Enter amount"
            helper_text_mode: "on_error"
            icon_right: "currency-eur"
            multiline: False
            required: True

        MDFillRoundFlatButton:
            text: "Add spending"
            md_bg_color: "grey"
            pos_hint: {"center_x": 0.5,"center_y": 0.5}
            on_release: 
                app.root.current = "main"
                root.add_income_or_spending(name_spending.text, amount_custom_spending.text)
                amount_custom_spending.text=""
                name_spending.text=""
    
<CustomIncome>:
    name: "custom_income"

    GridLayout:
        rows: 4
        
        MDLabel:
            text: "Add custom source of income"

        MDTextField:
            id: name_income
            helper_text: "Enter name"
            helper_text_mode: "on_error"
            multiline: False
            required: True

        MDTextField:
            id: amount_custom_income
            helper_text: "Enter amount"
            helper_text_mode: "on_error"
            icon_right: "currency-eur"
            multiline: False
            required: True

        MDFillRoundFlatButton:
            text: "Add income"
            md_bg_color: "grey"
            pos_hint: {"center_x": 0.5,"center_y": 0.5}
            on_release: 
                app.root.current = "main"
                root.add_income_or_spending(name_income.text, amount_custom_income.text)
                amount_custom_income.text=""
                name_income.text=""
    
            
<SettingsScreen>:
    name: "settings_screen"

    MDLabel:
        text: "Settings"
        halign: "center"
        valign: "center"
        theme_text_color: "Custom"
        text_color: "grey"

    MDFillRoundFlatButton:
        text: "Back"
        md_bg_color: "grey"
        pos_hint: {"center_x": 0.5,"center_y": 0.3}
        on_release: app.root.current = "main"

<InfoScreen>:
    name: "info_screen"

    MDLabel:
        text: "App info"
        halign: "center"
        valign: "center"
        theme_text_color: "Custom"
        text_color: "grey"
        
    MDFillRoundFlatButton:
        text: "Back"
        md_bg_color: "grey"
        pos_hint: {"center_x": 0.5,"center_y": 0.3}
        on_release: app.root.current = "main"

<AppThemeScreen>:
    name: "app_theme_screen"

    MDLabel:
        text: "App themes"
        halign: "center"
        valign: "center"
        theme_text_color: "Custom"
        text_color: "grey"
        
    MDFillRoundFlatButton:
        text: "Back"
        md_bg_color: "grey"
        pos_hint: {"center_x": 0.5,"center_y": 0.3}
        on_release: app.root.current = "main"
"""


class MainScreen(MDScreen):
    income_by_category = JsonStore("income_by_category_info.json")
    spending_by_category = JsonStore("spending_by_category_info.json")

    # ta funckcja teraz nie działa, trzeba tutaj dodać wczytywanie z plików spending_data i income_data
    def load_income_spending(self):
        print("hejka")
        for ID in self.spending_by_category:
            self.ids.card_layout.add_widget(
                MDCard(
                    MDLabel(text=f"numer ID: {ID}"),
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    padding="4dp",
                    size_hint=(None, None),
                    size=("200dp", "100dp"),
                )
            )

    def load_chart(self):
        self.name_list = []
        self.amount_list = []
        for name in self.spending_by_category:
            obj = self.spending_by_category.get(name)
            self.name_list.append(name)
            self.amount_list.append(obj["amount"])
        print(self.name_list, self.amount_list)
        plt.pie(x=self.amount_list, labels=self.name_list)
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # plt.show()
        # plt.savefig()


class SecondScreen(MDScreen):
    ID = 0
    ID_file = open("ID.txt", "r")
    # category_info_file = open("category_info.txt", "w+")

    if os.stat("ID.txt").st_size > 0:
        ID = int(ID_file.read())
        ID_file.close()

    def remove_marks(self, selected_chip, name):
        for chip in self.ids[name].children:
            if chip != selected_chip:
                chip.active = False

    def add_income_or_spending(self, amount_sent, chips, name):
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            self.ID_file = open("ID.txt", "w")
            if name == "income_box":
                self.stored_spending_or_income = JsonStore("income_data.json")
                self.spending_or_income_category_info = JsonStore(
                    "income_by_category_info.json"
                )
            elif name == "spending_box":
                self.stored_spending_or_income = JsonStore("spending_data.json")
                self.spending_or_income_category_info = JsonStore(
                    "spending_by_category_info.json"
                )
            for chip in chips:
                if chip.active:
                    self.stored_spending_or_income.put(
                        str(self.ID),
                        name=chip.text,
                        icon=chip.icon_right,
                        amount=self.amount,
                    )
                    if not self.spending_or_income_category_info.exists(chip.text):
                        self.spending_or_income_category_info.put(
                            chip.text, amount=self.amount
                        )
                    else:
                        self.spending_or_income_category_info.put(
                            chip.text,
                            amount=self.spending_or_income_category_info.get(chip.text)[
                                "amount"
                            ]
                            + self.amount,
                        )
                    self.ID += 1
                    self.ID_file.write(str(self.ID))
                    self.ID_file.close()


class CustomSpending(MDScreen):
    ID = 0
    ID_file = open("ID.txt", "r")
    # category_info_file = open("category_info.txt", "w+")

    if os.stat("ID.txt").st_size > 0:
        ID = int(ID_file.read())
        ID_file.close()

    def add_income_or_spending(self, name, amount_sent):
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            self.ID_file = open("ID.txt", "w")
            self.stored_spending_or_income = JsonStore("spending_data.json")
            self.spending_or_income_category_info = JsonStore(
                "spending_by_category_info.json"
            )
            self.stored_spending_or_income.put(
                str(self.ID),
                name=name,
                icon="",
                amount=self.amount,
            )
            if not self.spending_or_income_category_info.exists(name):
                self.spending_or_income_category_info.put(name, amount=self.amount)
            else:
                self.spending_or_income_category_info.put(
                    name,
                    amount=self.spending_or_income_category_info.get(name)["amount"]
                    + self.amount,
                )
            self.ID += 1
            self.ID_file.write(str(self.ID))
            self.ID_file.close()


class CustomIncome(MDScreen):
    ID = 0
    ID_file = open("ID.txt", "r")
    # category_info_file = open("category_info.txt", "w+")

    if os.stat("ID.txt").st_size > 0:
        ID = int(ID_file.read())
        ID_file.close()

    def add_income_or_spending(self, name, amount_sent):
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            self.ID_file = open("ID.txt", "w")
            self.stored_spending_or_income = JsonStore("income_data.json")
            self.spending_or_income_category_info = JsonStore(
                "income_by_category_info.json"
            )
            self.stored_spending_or_income.put(
                str(self.ID),
                name=name,
                icon="",
                amount=self.amount,
            )
            if not self.spending_or_income_category_info.exists(name):
                self.spending_or_income_category_info.put(name, amount=self.amount)
            else:
                self.spending_or_income_category_info.put(
                    name,
                    amount=self.spending_or_income_category_info.get(name)["amount"]
                    + self.amount,
                )
            self.ID += 1
            self.ID_file.write(str(self.ID))
            self.ID_file.close()


class SettingsScreen(MDScreen):
    pass


class InfoScreen(MDScreen):
    pass


class AppThemeScreen(MDScreen):
    pass


class WindowManager(ScreenManager):
    pass


class Budget_for_dummies(MDApp):
    def build(self):
        self.title = "Budget for Dummies"
        Window.top = 100
        Window.right = 100
        Window.size = (450, 700)
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        MainScreen().load_income_spending()


if __name__ == "__main__":
    Budget_for_dummies().run()
