import os.path

from kivy.storage.jsonstore import JsonStore

from kivymd.uix.screen import MDScreen


class SecondScreen(MDScreen):
    ID = 0
    ID_file = open("ID.txt", "r")

    if os.stat("ID.txt").st_size > 0:
        ID = int(ID_file.read())
        ID_file.close()

    def remove_marks(self, selected_chip, name):
        for chip in self.ids[name].children:
            if chip != selected_chip:
                chip.active = False

    def add_income_or_spending(self, amount_sent, chips, name, date):
        try:
            self.amount = float(amount_sent)
        except ValueError:
            print("Błąd podanych danych")
        else:
            self.spending_income = JsonStore("spending_income.json")
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
                        date=str(date),
                    )
                    self.spending_income.put(
                        str(self.ID),
                        type=name.strip("_box"),
                        name=chip.text,
                        icon=chip.icon_right,
                        amount=self.amount,
                        date=str(date),
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
