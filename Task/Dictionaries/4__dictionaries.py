player = {"name": "Ihor", "level": 19}


task = input("Ви виконали квест? так або ні:")

if task == "yes":
    player ["level"] += 1 
    print("Вітаємо! Ваш новий рівень: ",player["level"])
elif task=="no":
    print("Треба ще попрацювати")
else:
    print("Такого значення немає")

