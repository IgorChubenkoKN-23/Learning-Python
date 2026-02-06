coorect_pin="1234"
attempts = 3


while attempts > 0 :
 pin = input("Введіть пінкод")
 if pin == coorect_pin:
        print("Доступ дозволено")
        break
 elif pin!=coorect_pin:
    attempts-=1
    print("Залишилось спроб",attempts)
        
else:
   print("Картку заблоковано. Зверніться у банк.")
