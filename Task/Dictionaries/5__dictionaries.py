dormitory = { 
        "shevchenko": "402",
        "ivanov":"105",
        "bondar":"310"
        }

people = input("Введіть своє прізвище: ").strip().lower()

if people in dormitory:
    print("Проходьте ваша кімната",dormitory[people])
else:
    print("Такого студента в базі немає. Викличте чергового!")
