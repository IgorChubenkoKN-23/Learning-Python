forbidden_words = {"спам", "реклама", "казино"}


word = input("Введіть слово ")


if word in forbidden_words:
    print("Доступ заборонено")
else:
    print("Все добре")