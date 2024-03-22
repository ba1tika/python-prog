def num(num):
    i=1
    while i < num:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            return True
        i+=1
    return False


if __name__ == "__main__":
    try:
        c = int(input("Введите число:\n"))
        if c<1:
            print("Введите число больше или равно 1!!!!!!")
            exit(0)
    except ValueError:
        print("Введите целое число!!!!!!!")
        exit(0)
    print(num(c))


