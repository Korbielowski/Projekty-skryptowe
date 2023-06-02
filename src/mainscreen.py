from editspending import EditSpending
from editincome import EditIncome

from matplotlib import pyplot as plt

from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from kivymd.uix.label.label import MDIcon
from kivy.uix.image import Image
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import RelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.stacklayout import StackLayout
from kivymd.uix.button.button import MDFloatingActionButton
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.relativelayout import MDRelativeLayout


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

        self.stats_grid = BoxLayout(
            spacing=5,
            orientation="vertical",
        )  # GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.stats_grid.bind(minimum_height=self.stats_grid.setter("height"))
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
        print("Data loaded")
        spending_income = JsonStore("spending_income.json")
        # spending_data = JsonStore("spending_data.json")
        # income_data = JsonStore("income_data.json")
        self.ids.card_layout.clear_widgets()
        for ID in spending_income:
            if spending_income.get(ID)["type"] == "spending":
                self.ids.card_layout.add_widget(
                    MDCard(
                        MDRelativeLayout(
                            MDIcon(
                                icon=str(spending_income.get(ID)["icon"]),
                                pos_hint={"top": 0.6, "right": 0.4},
                            ),
                            MDLabel(
                                text=str(spending_income.get(ID)["name"])
                                + "  -"
                                + str(spending_income.get(ID)["amount"])
                                + " zł"
                            ),
                            MDRectangleFlatIconButton(
                                id=f"btn{ID}spending",
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
                                id=f"{ID}spending",
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
            elif spending_income.get(ID)["type"] == "income":
                self.ids.card_layout.add_widget(
                    MDCard(
                        MDRelativeLayout(
                            MDIcon(
                                icon=str(spending_income.get(ID)["icon"]),
                                pos_hint={"top": 0.6, "right": 0.4},
                            ),
                            MDLabel(
                                text=str(spending_income.get(ID)["name"])
                                + "  +"
                                + str(spending_income.get(ID)["amount"])
                                + " zł"
                            ),
                            MDRectangleFlatIconButton(
                                id=f"btn{ID}income",
                                theme_text_color="Custom",
                                line_color="grey",
                                text_color="grey",
                                icon_color="grey",
                                icon="pencil",
                                text="Edit",
                                pos_hint={"top": 0.75, "right": 0.7},
                                on_release=self.change_screen_to_edit_income_screen,
                            ),
                            MDRectangleFlatIconButton(
                                id=f"{ID}income",
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
        plt.clf()
        plt.pie(
            x=self.spending_amount_list,
            labels=self.spending_name_list,
            autopct="%1.1f%%",
            labeldistance=0.3,
            pctdistance=1.2,
        )
        plt.savefig("pie.jpg")
        image = Image(
            source="pie.jpg",
            allow_stretch=True,
            size_hint=(1, 1),
        )
        image.reload()
        # plt.clf()
        # width = 0.35
        # plt.bar(1, self.spending_total_amount, width, label="spendings")
        # plt.bar(1 + width, self.income_total_amount, width, label="income")
        # plt.xticks(positions, self.spending_name_list)
        # plt.legend()
        # plt.savefig("bar.jpg")
        # box.add_widget(Image(source="bar.jpg"))
        # box.add_widget(Image(source="pie.jpg"))
        box = self.ids.stats_layout
        box.clear_widgets()
        box.add_widget(image)
        # box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # plt.clf()
        # plt.pie(
        #     x=self.spending_amount_list,
        #     labels=self.spending_name_list,
        #     autopct="%1.1f%%",
        #     labeldistance=0.3,
        #     pctdistance=1.2,
        # )
        # box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # box.add_widget(MDLabel(text="Hejka"))
        # print("Loaded chart")

    def delete_data(self, instance):
        # type = ""
        ID = ""
        income_data = JsonStore("income_data.json")
        income_by_category = JsonStore("income_by_category_info.json")
        spending_income = JsonStore("spending_income.json")
        spending_data = JsonStore("spending_data.json")
        spending_by_category = JsonStore("spending_by_category_info.json")

        if "income" in instance.id:
            ID = instance.id.strip("income")
            # type = instance.id.strip(ID)
        elif "spending" in instance.id:
            ID = instance.id.strip("spending")
            # type = instance.id.strip(ID)

        if ID in spending_data:
            new_amount = (
                spending_by_category.get(spending_data.get(ID)["name"])["amount"]
                - spending_data.get(ID)["amount"]
            )
            if new_amount <= 0:
                spending_by_category.delete(spending_data.get(ID)["name"])
            else:
                spending_by_category.put(
                    spending_data.get(ID)["name"], amount=new_amount
                )
            spending_data.delete(ID)
            self.ids.card_layout.remove_widget(instance.parent)
        elif ID in income_data:
            new_amount = (
                income_by_category.get(income_data.get(ID)["name"])["amount"]
                - income_data.get(ID)["amount"]
            )

            if new_amount <= 0:
                income_by_category.delete(income_data.get(ID)["name"])
            else:
                income_by_category.put(income_data.get(ID)["name"], amount=new_amount)
            income_data.delete(ID)
            self.ids.card_layout.remove_widget(instance.parent)
        spending_income.delete(ID)
        self.load_income_spending()

    def change_screen_to_edit_spending_screen(self, instance=None):
        btn = instance.id.strip("btn")
        edit_screen = EditSpending()
        edit_screen.save_ID_type(btn)
        # save_ID(btn_ID)
        self.manager.current = "edit_spending_screen"

    def change_screen_to_edit_income_screen(self, instance=None):
        btn = instance.id.strip("btn")
        edit_income_screen = EditIncome()
        edit_income_screen.save_ID_type(btn)
        # save_ID(btn_ID)
        self.manager.current = "edit_income_screen"

    def change_screen_to_second(self, instance=None):
        self.manager.current = "second"

    def change_screen_to_settings_screen(self, instance=None):
        self.manager.current = "settings_screen"

    def change_screen_to_info_screen(self, instance=None):
        self.manager.current = "info_screen"

    def change_screen_to_app_theme_screen(self, instance=None):
        self.manager.current = "app_theme_screen"
