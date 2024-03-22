import cowsay
def division(num, den):
    i = 1
    while i <= num:
        if num % i == 0 and den % i == 0:
            num = num / i
            den = den / i
        i += 1
    output = str(int(num)) + "/" + str(int(den))
    return output


num1 = int(input("Введите числитель:\n"))
num2 = int(input("Введите знаменатель:\n"))
if num2 == 0:
    print("Знаменатель не может быть равен 0")
    exit(0)

cowsay.cow(division(num1, num2))

