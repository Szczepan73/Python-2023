#------Zadanie 2


liczba = 0

nazwy_jednosci = {0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_nast = {10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście", 16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście",
                  19: "dziewiętnaście"}
nazwy_dziesiatek = {2: "dwadzieścia", 3: "trzydzieści", 4: "czterdzieści", 5: "pięćdziesiąt", 6: "sześćdziesiąt", 7: "siedemdziesiąt", 8: "osiemdziesiąt", 9: "dziewięćdziesiąt"}




liczba = int(input("Wpisz cyfre"))


d = int(liczba) // 10
j = int(liczba) % 10

if d == 0 :
    a = nazwy_jednosci[j]
    print(a)
elif d == 1:
    z = nazwy_nast[liczba]
    print (z)
else :
    koniec = nazwy_dziesiatek[d] + " " + nazwy_jednosci[j]
    print (koniec)