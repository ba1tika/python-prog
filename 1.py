
def sum(trace):
    price = 4 + (int(trace) // 140) * 0.25
    output = str(price) + "$"
    return "С вас :  " + output


print(sum(input("Введите расстояние в метрах:\n")))
