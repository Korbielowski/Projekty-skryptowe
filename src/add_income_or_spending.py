from kivy.storage.jsonstore import JsonStore

ID = 0


def add_income_or_spending(amount_sent, chips, name):
    try:
        amount = float(amount_sent)
    except ValueError:
        print("Błąd podanych danych")
    else:
        ID_file = open("ID.txt", "w")
        if name == "income_box":
            stored_spending_or_income = JsonStore("income_data.json")
            spending_or_income_category_info = JsonStore("income_by_category_info.json")
        elif name == "spending_box":
            stored_spending_or_income = JsonStore("spending_data.json")
            spending_or_income_category_info = JsonStore(
                "spending_by_category_info.json"
            )
        for chip in chips:
            if chip.active:
                stored_spending_or_income.put(
                    str(ID),
                    name=chip.text,
                    icon=chip.icon_right,
                    amount=amount,
                )
                if not spending_or_income_category_info.exists(chip.text):
                    spending_or_income_category_info.put(chip.text, amount=amount)
                else:
                    spending_or_income_category_info.put(
                        chip.text,
                        amount=spending_or_income_category_info.get(chip.text)["amount"]
                        + amount,
                    )
                ID += 1
                ID_file.write(str(ID))
                ID_file.close()
