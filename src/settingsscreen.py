from kivymd.uix.list import MDList
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.scrollview import MDScrollView


class SettingsScreen(MDScreen):
    def on_pre_enter(self):
        self.currencies = ["$", "€", "£", "¥", "₣", "zł"]
        self.view = MDScrollView()
        self.list = MDList()
        self.ids["list"] = self.list
        self.view.add_widget(self.list)
        for cur in self.currencies:
            self.list.add_widget(
                OneLineListItem(text=cur, id=cur, on_release=self.save_to_file)
            )
        self.add_widget(self.view)

    def save_to_file(self, instance=None):
        self.file = open("currency.txt", "w")
        self.currency = str(instance.id)
        print(f"Something happened: {instance.id}")
        # self.file.write(self.currency)
