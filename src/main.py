import json
import os.path
from datetime import datetime

from matplotlib import pyplot as plt

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from kivymd.app import MDApp
from kivymd.uix.label.label import MDIcon
from kivy.uix.button import Button
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.relativelayout import RelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.stacklayout import StackLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button.button import MDFloatingActionButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.relativelayout import MDRelativeLayout


KV = """
<MainScreen>:
    # on_enter: print("hejka")

    # MDBottomNavigation:
    #     selected_color_background: "orange"
    #     text_color_active: "lightgrey"

    #     MDBottomNavigationItem:
    #         id: "home"
    #         name: "home"
    #         text: "home"
    #         icon: "home"
    #         on_enter: root.load_income_spending()
            
    #         # ScrollView:
    #         #     do_scroll_x: False
    #         #     do_scroll_y: True
    #         #     # size_hint: 1, None
    #         #     # size: Window.width, Window.height

    #         #     GridLayout:
    #         #         id: card_layout
    #         #         clos: 1
    #         #         rows: 30
    #         #         size_hint: 1, None
    #         #         # minimum_height: 
                    
    #         MDFloatingActionButton:
    #             icon: "plus"
    #             pos_hint: {"center_x": 0.915,"center_y": 0.06}
    #             icon_color: "grey"
    #             md_bg_color: "white"
    #             on_release: app.root.current = "second"

    #     MDBottomNavigationItem:
    #         name: "stats"
    #         text: "stats"
    #         icon: "chart-bar"
    #         on_pre_enter:
    #             root.load_chart()

    #         BoxLayout:
    #             id: box
    #             size_hint_y: .8
    #             pos_hint: {"top":1}

            # MDLabel:
            #     text: "Charts and stats"
            #     halign: "center"
            #     valign: "center"
            #     theme_text_color: "Custom"
            #     text_color: "grey"

        # MDBottomNavigationItem:
        #     name: "more"
        #     text: "more"
        #     icon: "dots-horizontal"

        #     StackLayout:
        #         MDRectangleFlatIconButton:
        #             icon: "cog"
        #             text: "Settings"
        #             size_hint: 0.3333, 0.3333
        #             theme_text_color: "Custom"
        #             line_color: "grey"
        #             text_color: "grey"
        #             icon_color: "grey"
        #             on_release: app.root.current = "settings_screen"

        #         MDRectangleFlatIconButton:
        #             icon: "information"
        #             text: "Info"
        #             size_hint: 0.3333, 0.3333
        #             theme_text_color: "Custom"
        #             line_color: "grey"
        #             text_color: "grey"
        #             icon_color: "grey"
        #             on_release: app.root.current = "info_screen"

        #         MDRectangleFlatIconButton:
        #             icon: "palette"
        #             text: "App Theme"
        #             size_hint: 0.3333, 0.3333
        #             theme_text_color: "Custom"
        #             line_color: "grey"
        #             text_color: "grey"
        #             icon_color: "grey"
        #             on_release: app.root.current = "app_theme_screen"

<SecondScreen>:
    
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
                        on_press:
                            root.remove_marks(self, "spending_box")
                            app.root.current = "custom_spending"

                MDFillRoundFlatButton:
                    text: "Add spending"
                    md_bg_color: "grey"
                    pos_hint: {"center_x": 0.5,"center_y": 0.8}
                    on_release:
                        root.add_income_or_spending(amount_spending.text, spending_box.children, "spending_box")
                        root.remove_marks(self, "spending_box")
                        amount_spending.text=""
                        app.root.current = "main"

                MDFillRoundFlatButton:
                    text: "Back"
                    md_bg_color: "grey"
                    pos_hint: {"center_x": 0.5,"center_y": 0.2}
                    on_release: 
                        root.remove_marks(self, "spending_box")
                        app.root.current = "main"

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
                        root.add_income_or_spending(amount_income.text, income_box.children, "income_box")
                        root.remove_marks(self, "income_box")
                        amount_income.text=""
                        app.root.current = "main"

                MDFillRoundFlatButton:
                    text: "Back"
                    md_bg_color: "grey"
                    pos_hint: {"center_x": 0.5,"center_y": 0.2}
                    on_release: 
                        root.remove_marks(self, "income_box")
                        app.root.current = "main"
<CustomSpending>:

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
    
<EditSpending>:
        
    BoxLayout:
        orientation: "vertical"
    
        MDLabel:
            text: "Edit spending"

        MDTextField:
            id: name_spending
            helper_text: "Enter name"
            helper_text_mode: "on_error"
            multiline: False
            required: True

        MDTextField:
            id: amount_spending
            helper_text: "Enter amount"
            helper_text_mode: "on_error"
            icon_right: "currency-eur"
            multiline: False
            required: True
        GridLayout:
            cols: 2
            rows: 1

            
            MDFillRoundFlatButton:
                text: "Edit spending"
                md_bg_color: "grey"
                # pos_hint: {"center_x": 0.5,"center_y": 0.5}
                on_release: 
                    app.root.current = "main"
                    root.change_income_or_spending(name_spending.text, amount_spending.text)
                    amount_spending.text=""
                    name_spending.text=""

            MDFillRoundFlatButton:
                text: "Back"
                md_bg_color: "grey"
                # pos_hint: {"center_x": 0.5,"center_y": 0.5}
                on_release: 
                    app.root.current = "main"
                    amount_spending.text=""
                    name_spending.text=""

<SettingsScreen>:

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

# btn_ID = 0


class MainScreen(MDScreen):
    # spending_data = JsonStore(
    #     "spending_data.json"
    # )  # Dodać żeby było w funkcjach, bo tak to zmienne się nie aktualizują
    # income_data = JsonStore("income_data.json")
    # income_by_category = JsonStore("income_by_category_info.json")
    # spending_by_category = JsonStore("spending_by_category_info.json")

    def on_pre_enter(self):
        self.navigation = MDBottomNavigation(
            selected_color_background="orange", text_color_active="lightgrey"
        )
        self.navigation_item_home = MDBottomNavigationItem(
            name="home", text="home", icon="home"
        )
        self.navigation_item_stats = MDBottomNavigationItem(
            name="stats", text="stats", icon="chart-bar", on_enter=self.load_chart
        )
        self.navigation_item_more = MDBottomNavigationItem(
            name="more",
            text="more",
            icon="dots-horizontal",
        )

        self.ids["stats"] = self.navigation_item_stats
        self.ids["home"] = self.navigation_item_home
        self.ids["more"] = self.navigation_item_more

        self.navigation.add_widget(self.navigation_item_home)
        self.navigation.add_widget(self.navigation_item_stats)
        self.navigation.add_widget(self.navigation_item_more)

        self.scroll_home = ScrollView(
            size_hint=(1, None),
            size=(Window.width, Window.height - Window.height * 0.12),
        )

        self.scroll_stats = ScrollView(
            size_hint=(1, None),
            size=(Window.width, Window.height - Window.height * 0.12),
        )

        self.card_grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.card_grid.bind(minimum_height=self.card_grid.setter("height"))
        self.ids["card_layout"] = self.card_grid

        self.stats_grid = RelativeLayout()
        # self.stats_grid.bind(minimum_height=self.stats_grid.setter("height"))
        self.ids["stats_layout"] = self.stats_grid

        self.more_grid = StackLayout()
        self.ids["more_layout"] = self.more_grid

        self.add_button = MDFloatingActionButton(
            icon="plus",
            icon_color="grey",
            md_bg_color="white",
            pos_hint={"center_x": 0.915, "center_y": 0.06},
        )
        self.add_button.bind(on_release=self.change_screen_to_second)

        self.settings_button = MDRectangleFlatIconButton(
            text="Settings",
            icon="cog",
            size_hint=(0.3333, 0.3333),
            theme_text_color="Custom",
            line_color="grey",
            text_color="grey",
            icon_color="grey",
            on_release=self.change_screen_to_settings_screen,
        )
        self.info_button = MDRectangleFlatIconButton(
            text="Info",
            icon="information",
            size_hint=(0.3333, 0.3333),
            theme_text_color="Custom",
            line_color="grey",
            text_color="grey",
            icon_color="grey",
            on_release=self.change_screen_to_info_screen,
        )
        self.app_theme_button = MDRectangleFlatIconButton(
            text="App theme",
            icon="palette",
            size_hint=(0.3333, 0.3333),
            theme_text_color="Custom",
            line_color="grey",
            text_color="grey",
            icon_color="grey",
            on_release=self.change_screen_to_app_theme_screen,
        )

        self.more_grid.add_widget(self.settings_button)
        self.more_grid.add_widget(self.info_button)
        self.more_grid.add_widget(self.app_theme_button)

        self.scroll_home.add_widget(self.card_grid)
        self.ids.home.add_widget(self.scroll_home)
        self.ids.home.add_widget(self.add_button)

        self.scroll_stats.add_widget(self.stats_grid)
        self.ids.stats.add_widget(self.scroll_stats)

        self.ids.more.add_widget(self.more_grid)

        self.add_widget(self.navigation)

        self.load_income_spending()
        self.load_chart()

    def load_income_spending(self):
        print("Załadowano dane")
        spending_data = JsonStore("spending_data.json")
        self.ids.card_layout.clear_widgets()
        for ID in spending_data:
            self.ids.card_layout.add_widget(
                MDCard(
                    MDRelativeLayout(
                        MDIcon(
                            icon=str(spending_data.get(ID)["icon"]),
                            pos_hint={"top": 0.6, "right": 0.4},
                        ),
                        MDLabel(
                            text=str(spending_data.get(ID)["name"]),
                            # pos_hint={"top": 0.6, "right": 0.1},
                        ),
                        MDRectangleFlatIconButton(
                            id=f"btn{ID}",
                            theme_text_color="Custom",
                            line_color="grey",
                            text_color="grey",
                            icon_color="grey",
                            icon="pencil",
                            text="Edit",
                            pos_hint={"top": 0.75, "right": 0.7},
                            on_release=self.change_screen_to_edit_spending_screen,
                        ),
                        MDRectangleFlatIconButton(
                            id=str(ID),
                            theme_text_color="Custom",
                            line_color="grey",
                            text_color="grey",
                            icon_color="grey",
                            icon="delete",
                            text="Delete",
                            pos_hint={"top": 0.75, "right": 0.95},
                            on_release=self.delete_data,
                        ),
                    ),
                    id="Card{ID}",
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    # pos_hint={"left": 1, "top": 1},
                    padding="4dp",
                    size_hint=(1, None),
                    size=("200dp", "100dp"),
                ),
            ),

    def load_chart(self, instance=None):
        spending_by_category = JsonStore("spending_by_category_info.json")
        income_by_category = JsonStore("income_by_category_info.json")
        self.spending_name_list = []
        self.spending_amount_list = []
        self.income_name_list = []
        self.income_amount_list = []
        for name in spending_by_category:
            obj = spending_by_category.get(name)
            self.spending_name_list.append(name)
            self.spending_amount_list.append(obj["amount"])

        for name in income_by_category:
            obj = income_by_category.get(name)
            self.income_name_list.append(name)
            self.income_amount_list.append(obj["amount"])

        self.spending_total_amount = sum(self.spending_amount_list)
        self.income_total_amount = sum(self.income_amount_list)
        # print(self.spending_total_amount)
        # print(self.income_total_amount)
        plt.clf()
        plt.pie(
            x=self.spending_amount_list,
            labels=self.spending_name_list,
            autopct="%1.1f%%",
            labeldistance=0.3,
            pctdistance=1.2,
        )
        # plt.savefig("pie.png")
        # plt.clf()
        # width = 0.35
        # plt.bar(1, self.spending_total_amount, width, label="spendings")
        # plt.bar(1 + width, self.income_total_amount, width, label="income")
        # plt.xticks(positions, self.spending_name_list)
        # plt.legend()
        # plt.savefig("bar.png")
        # box.add_widget(Image(source="bar.png"))
        # box.add_widget(Image(source="pie.png"))
        box = self.ids.stats_layout
        box.clear_widgets()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # print("Załadowano wykres")

    def delete_data(self, instance):
        spending_data = JsonStore("spending_data.json")
        spending_by_category = JsonStore("spending_by_category_info.json")
        if instance.id in spending_data:
            # parent_id = f"Card{instance.id}"
            new_amount = (
                spending_by_category.get(spending_data.get(instance.id)["name"])[
                    "amount"
                ]
                - spending_data.get(instance.id)["amount"]
            )
            if new_amount <= 0:
                spending_by_category.delete(spending_data.get(instance.id)["name"])
            else:
                spending_by_category.put(
                    spending_data.get(instance.id)["name"], amount=new_amount
                )
            spending_data.delete(instance.id)
            self.ids.card_layout.remove_widget(instance.parent)
            self.load_income_spending()
            # instance.parent.parent.remove_widget(instance.parent)

    def change_screen_to_second(self, instance=None):
        self.manager.current = "second"
        print("wykonano")

    def change_screen_to_edit_spending_screen(self, instance=None):
        # self.manager.current = "edit_spending_screen"
        global btn_ID
        btn_ID = instance.id.strip("btn")
        self.manager.current = "edit_spending_screen"

    def change_screen_to_settings_screen(self, instance=None):
        self.manager.current = "settings_screen"

    def change_screen_to_info_screen(self, instance=None):
        self.manager.current = "info_screen"

    def change_screen_to_app_theme_screen(self, instance=None):
        self.manager.current = "app_theme_screen"


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


class EditSpending(MDScreen):
    def change_income_or_spending(self, name, amount_sent):
        self.stored_spending_or_income = JsonStore("spending_data.json")
        self.spending_or_income_category_info = JsonStore(
            "spending_by_category_info.json"
        )
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            self.icon = self.stored_spending_or_income.get(btn_ID)["icon"]
            self.name = self.stored_spending_or_income.get(btn_ID)["name"]
            self.amount_get = self.stored_spending_or_income.get(btn_ID)["amount"]
            self.amount_from_category = self.spending_or_income_category_info.get(
                self.name
            )["amount"]
            self.stored_spending_or_income.put(
                btn_ID, name=name, icon=self.icon, amount=self.amount
            )
            if (
                self.spending_or_income_category_info.get(self.name)["amount"]
                - self.amount_get
                <= 0
            ):
                self.spending_or_income_category_info.delete(self.name)
                self.spending_or_income_category_info.put(name, amount=self.amount)
            else:
                self.spending_or_income_category_info.put(
                    self.name, amount=self.amount_from_category - self.amount_get
                )
                self.spending_or_income_category_info.put(name, amount_sent)


class EditIncome(MDScreen):
    def change_income_or_spending(self, name, amount_sent):
        self.stored_spending_or_income = JsonStore("income_data.json")
        self.spending_or_income_category_info = JsonStore(
            "income_by_category_info.json"
        )
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            self.icon = self.stored_spending_or_income.get(btn_ID)["icon"]
            self.name = self.stored_spending_or_income.get(btn_ID)["name"]
            self.amount_get = self.stored_spending_or_income.get(btn_ID)["amount"]
            self.amount_from_category = self.spending_or_income_category_info.get(
                self.name
            )["amount"]
            self.stored_spending_or_income.put(
                btn_ID, name=name, icon=self.icon, amount=self.amount
            )
            if (
                self.spending_or_income_category_info.get(self.name)["amount"]
                - self.amount_get
                <= 0
            ):
                self.spending_or_income_category_info.delete(self.name)
                self.spending_or_income_category_info.put(name, amount=self.amount)
            else:
                self.spending_or_income_category_info.put(
                    self.name, amount=self.amount_from_category - self.amount_get
                )
                self.spending_or_income_category_info.put(name, amount_sent)


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
        Builder.load_string(KV)
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(SecondScreen(name="second"))
        sm.add_widget(CustomSpending(name="custom_spending"))
        sm.add_widget(CustomIncome(name="custom_income"))
        sm.add_widget(EditSpending(name="edit_spending_screen"))
        sm.add_widget(SettingsScreen(name="settings_screen"))
        sm.add_widget(InfoScreen(name="info_screen"))
        sm.add_widget(AppThemeScreen(name="app_theme_screen"))
        return sm


sm = ScreenManager()


if __name__ == "__main__":
    Budget_for_dummies().run()
