

def get_final_price(price):
    if price> 1000:
        price*=0.9
        print("Знижка 10%",price)
    elif price > 500 and price < 1000:
        price*=0.95
        print("Знижка 5%",price)
    else:
        print("Ціна: ",price)
    
    return price

orders = [1200,300,800]


for number in orders:
    get_final_price(number)
