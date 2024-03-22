import random

alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alph = list(alph)
r= random.randrange(0,2)
if r:
    k= alph[random.randrange(0,33)]
    k += alph[random.randrange(0,33)]
    k += alph[random.randrange(0, 33)]
    k += str(random.randrange(0, 10))
    k += str(random.randrange(0, 10))
    k += str(random.randrange(0, 10))
else:
    k = str(random.randrange(0, 10))
    k += str(random.randrange(0, 10))
    k += str(random.randrange(0, 10))
    k += str(random.randrange(0, 10))
    k+=alph[random.randrange(0,33)]
    k+=alph[random.randrange(0,33)]
    k+=alph[random.randrange(0,33)]
print(k)
