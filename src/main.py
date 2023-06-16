from editincome import EditIncome
from infoscreen import InfoScreen
from mainscreen import MainScreen
from customincome import CustomIncome
from editspending import EditSpending
from secondscreen import SecondScreen
from appthemescreen import AppThemeScreen
from customspending import CustomSpending
from settingsscreen import SettingsScreen

from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager


class Budget_for_dummies(MDApp):
    def build(self):
        self.title = "Budget for Dummies"
        Window.top = 100
        Window.right = 100
        Window.size = (450, 700)
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        Builder.load_file("Budget_for_dummies.kv")
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(SecondScreen(name="second"))
        sm.add_widget(CustomSpending(name="custom_spending"))
        sm.add_widget(CustomIncome(name="custom_income"))
        sm.add_widget(EditSpending(name="edit_spending_screen"))
        sm.add_widget(EditIncome(name="edit_income_screen"))
        sm.add_widget(SettingsScreen(name="settings_screen"))
        sm.add_widget(InfoScreen(name="info_screen"))
        sm.add_widget(AppThemeScreen(name="app_theme_screen"))
        return sm


sm = ScreenManager()


if __name__ == "__main__":
    Budget_for_dummies().run()
