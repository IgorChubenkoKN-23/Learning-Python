def matematik (number1,number2):
    res1=number1-number2
    res2=number1+number2
    print(res1,res2)
    return res1,res2


result = matematik(40,20)
print(result)
print(type(result))

difference,suma = result

print("Різниця",difference)
print("Сума",suma)