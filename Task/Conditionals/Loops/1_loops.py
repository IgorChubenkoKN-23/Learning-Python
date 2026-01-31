dormitory = { 
        "Shevchenko": "402",
        "Ivanov":"105",
        "Bondar":"310"
        }

for last_name,room in dormitory.items():
    print(f"Шановний {last_name},завтра о 10:00 ремонтні роботи у вашій кімнаті{room}")