
while True :
    command=int(input("Введіть роки")) 
    match command:
        case 1 :
            print('Малюк')
        case 2:
            print('''See you later
                Як ви
                хто ви''')
        case 20:
            print('Сформований')
        case 40:
            print('Більше сормований')
        case 80:
            print('Риєм глину')
            
        case other:
            print('Ноу коментс')
            if command> 101:
                break