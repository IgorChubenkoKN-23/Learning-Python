dormitory = { 
        "Shevchenko": "402",
        "Ivanov":"105",
        "Bondar":"310"
        }

people = input("Введіть своє прізвище: ")

if people in dormitory:
    print("Проходьте ваша кімната",dormitory[people])
else:
    print("Такого студента в базі немає. Викличте чергового!")
