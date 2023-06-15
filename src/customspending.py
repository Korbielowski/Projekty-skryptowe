import os.path

from kivy.storage.jsonstore import JsonStore

from kivymd.uix.screen import MDScreen


class CustomSpending(MDScreen):
    ID = 0
    ID_file = open("ID.txt", "r")

    if os.stat("ID.txt").st_size > 0:
        ID = int(ID_file.read())
        ID_file.close()

    def add_income_or_spending(self, name, amount_sent, type, date):
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            self.ID_file = open("ID.txt", "w")
            self.spending_income = JsonStore("spending_income.json")
            self.stored_spending_or_income = JsonStore("spending_data.json")
            self.spending_or_income_category_info = JsonStore(
                "spending_by_category_info.json"
            )
            self.stored_spending_or_income.put(
                str(self.ID),
                name=name,
                icon="",
                amount=self.amount,
                date=str(date),
            )
            self.spending_income.put(
                str(self.ID),
                type=type,
                name=name,
                icon="",
                amount=self.amount,
                date=str(date),
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
