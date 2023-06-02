from kivy.storage.jsonstore import JsonStore

from kivymd.uix.screen import MDScreen


class EditSpending(MDScreen):
    def save_ID_type(self, btn=None):
        global btn_ID
        global type
        btn_ID = btn.strip("spending")
        type = btn.strip(btn_ID)
        # print("Wysłane ID:", )

    def change_income_or_spending(self, name, amount_sent):
        # btn_ID = load_ID()
        self.spending_income = JsonStore("spending_income.json")
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
            self.date = self.stored_spending_or_income.get(btn_ID)["date"]
            self.amount_get = self.stored_spending_or_income.get(btn_ID)["amount"]
            self.amount_from_category = self.spending_or_income_category_info.get(
                self.name
            )["amount"]
            self.stored_spending_or_income.put(
                btn_ID,
                name=name,
                icon=self.icon,
                amount=self.amount,
                date=self.date,
            )
            self.spending_income.put(
                btn_ID,
                type=type,
                name=name,
                icon=self.icon,
                amount=self.amount,
                date=self.date,
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
            # self.manager.current = "main"
