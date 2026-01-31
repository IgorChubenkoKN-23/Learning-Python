bills = {
    "Ivanov": 250,
    "Petrov": 0,
    "Sidorov": 500,
    "Bondar": 0,
    "Kuzmenko": 120
}

debrotors_list= []
total_sum = 0 


for last_name, debt in bills.items():
    if debt>0:
        print(f"{last_name} заборгованість {debt}")
        total_sum += debt
        if debt>200:
            debrotors_list.append(last_name)
    else:
        print(f"{last_name}: Дякуємо за оплату!")

print("Загальна вартість", total_sum)
print("Боржники 200+ боргом",debrotors_list)