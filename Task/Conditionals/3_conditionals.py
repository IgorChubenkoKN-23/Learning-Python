# Початкові дані для перевірки
correct_password = "Python2026"

age = int(input("Введіть ваш вік: "))
password = input("Введіть пароль: ")
status = input("Ваш статус (адмін/гість): ").lower().strip()


if age >= 18:
    if  password == correct_password :
        print("Пароль коректний ")
   
        if status == "адмін":
                print("Вітаємо, пане Адмін! Повний доступ надано")
        elif status == "гість" :
                print("Вітаємо! Обмежений доступ надано")
        else:
            print("Статус не розпізнано, доступ обмежено")
    else:
          print("Пароль не вірний ")

else:
    print("Вам нема 18")    