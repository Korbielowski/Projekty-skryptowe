from kivy.storage.jsonstore import JsonStore

stored_spending = JsonStore("spending_data.json")
object = []
for ID in stored_spending:
    stor = stored_spending.get(ID)
    object.append(stor["name"])
    object.append(stor["amount"])
print(object)
