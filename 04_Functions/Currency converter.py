def to_usd(uah_amount, rate):
 
    dollars = uah_amount / rate 
    return dollars

my_dollars = to_usd(1000,40)
print("Я отримав",my_dollars ,"Доларів")