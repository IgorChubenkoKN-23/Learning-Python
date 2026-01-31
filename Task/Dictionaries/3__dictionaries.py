#task 1 
secret_data={"password":"admin"}

corect_password=input("Введіть пароль для входу в систему: ")

if corect_password == secret_data["password"]:
    print("Доступ дозволено")
else:
    print(("Пароль не вірний"))


#task 2 
menu={
    "pizza":"250",
    "burger":"120",
    "pasta":"180"   
}


order=input("Введіть що бажаєте замовити")

if order in menu:
    print(order,menu[order])
else:
    print("Такої страви немає")


#task 3 
player = {"name": "Ihor", "level": 19}


task = input("Ви виконали квест? так або ні:")

if task == "yes":
    player ["level"] += 1 
    print("Вітаємо! Ваш новий рівень: ",player["level"])
elif task=="no":
    print("Треба ще попрацювати")
else:
    print("Такого значення немає")

