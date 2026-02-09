tariffs = {
    "польща": [344,455],
    "німеччина": [450, 110],
    "сша": [700,800]
}

country=input("Введіть країну доставки:")
mass=input("Введіть вагу посилки: ")


if int(mass) <= 5 :
    print(tariffs[country][0])
elif int(mass)> 5 :
    print(tariffs[country][1])
