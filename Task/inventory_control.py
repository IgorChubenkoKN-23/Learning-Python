sklad = [
    {"item": "Laptop", "count": 5, "price": 1200},
    {"item": "Mouse", "count": 0, "price": 25},
    {"item": "Monitor", "count": 2, "price": 300},
    {"item": "Keyboard", "count": 15, "price": 50}
]
number=0

for goods in sklad :
    number += goods["count"]
    if goods["count"] == 0:
        print("Товару немає в наявності")
    elif goods["count"] < 3:
        procurement = goods["price"]*10
        print("Сума закупівлі",procurement)
    elif goods["count"] >= 3 :
        print("Запасів достатньо")

print(number)