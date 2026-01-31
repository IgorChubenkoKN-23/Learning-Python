people = {"name": "Ihor"}
choice = input("Введи щось: ")

# Варіант 1 (шукає ключ)
if choice in people:
    print(f"Знайдено КЛЮЧ: {choice}")

# Варіант 2 (порівнює значення)
if choice == people["name"]:
    print(f"Знайдено ЗНАЧЕННЯ: {choice}")