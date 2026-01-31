admin_name="admin"
correct_password="1234"

name=input("Введіть імя :")
passsword=input("Введіть пароль")



if name == admin_name:
    if passsword != correct_password:
        print("Парольs не правильний")
    else:
        print("Ласкаво просимо в систему")
else:
    print("Імя користувача не коректне.")


