from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import MDList
from kivymd.uix.scrollview import MDScrollView


class SettingsScreen(MDScreen):
    def on_enter(self):
        self.add_widget(MDScrollView(MDList(id="list")))
        for i in range(20):
            self.ids.list.add_widget(OneLineListItem(text=f"siema {i}"))
