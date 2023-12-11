for i in range(12):
    print(i)

for i in range(3, 12):
    print(i)

for i in range(3, 12, 2):
    print(i)

for c in "Ala ma kota":
    print(c)

for i in range(10):
    print(i)
else:
    print("Koniec")

for i in range(10):
    print(i)
    if i > 6:
        break
else:
    print("Koniec")

















    i = int(input("podaj liczbę 2 cyfrową"))
    a = i // 10
    b = i % 10
    if (a + b) % 7 == 0 and i % 2 == 0:
        print(f'{i} Dobra liczba')
    else:
        print(f'{i} Zła liczba')





for i in range(1 , 100):

        a = i // 10
        b = i % 10
        if (a + b) % 7 == 0 and i % 2 == 0:
            print(f'{i} Dobra liczba')

else:
    print("Koniec")