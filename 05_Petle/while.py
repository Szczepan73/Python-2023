n = 5

while n > 0:
    print(n)
    n -= 1

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue
    print(f'{n} tak')


n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')
else:
    print('Koniec')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')
else:
    print('Koniec')


liczba = input()
suma = 0

for char in str(liczba):
    print (f"{char} oraz suma to {suma}")
    suma += int(char)
print(suma)


