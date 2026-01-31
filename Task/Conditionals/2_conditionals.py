tariffs = {
    "польща": 300,
    "німеччина": 450,
    "сша": 700
}

country=input("Введіть країну доставки:").strip().lower()
mass=input("Введіть вагу посилки: ")
    
if country == "Україна":
    if int(mass) <= 5 :
        print("Ціна 50 грн")
    elif int(mass)> 5 :
        print("Ціна 100 грн")
elif country in tariffs:
    print(f"Ціна {tariffs[country]} грн")
else:
    print("Доставка в цю країну недоступна")