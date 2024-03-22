

def sum(n):
    price=2.95*int(n)+10.95
    return "С вас: "+str(int(price)) + "$"


print(sum(input("Введите количество товара:\n")))
