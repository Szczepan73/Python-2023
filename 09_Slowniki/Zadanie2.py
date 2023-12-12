#------Zadanie 2


liczba = 0

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_nast = {10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście", 16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście",
                  19: "dziewiętnaście"}
nazwy_dziesiatek = {2: "dwadzieścia", 3: "trzydzieści", 4: "czterdzieści", 5: "pięćdziesiąt", 6: "sześćdziesiąt", 7: "siedemdziesiąt", 8: "osiemdziesiąt", 9: "dziewięćdziesiąt"}

nazwy_setek = {1: "sto", 2: "dwieście", 3: "trzysta", 4: "czterysta" , 5: "pięćset", 6: "sześćset", 7: "siedemset", 8: "osiemset", 9: "dziewięćset"}


#-------------------------------------------------------------------


liczba = int(input("Wpisz cyfre"))

g = int(liczba) // 100
d = (liczba % 100 ) // 10
j = liczba % 10
lista_2 = []
if g != 0:
    lista_2.append(nazwy_setek[g])
if d == 1:
    lista_2.append(nazwy_nast[liczba % 100])
else:
    lista_2.append(nazwy_dziesiatek[d])
    lista_2.append(nazwy_jednosci[j])
print (" ".join(lista_2) )


#-------------------------------------------------------------------


if g == 0:

    if d == 0:
        a = nazwy_jednosci[j]
        print(a)
    elif d == 1:
        z = nazwy_nast[liczba]
        print (z)
    else :
        koniec = nazwy_dziesiatek[d] + " " + nazwy_jednosci[j]
        print (koniec)
else:

    if d == 0:
        a = nazwy_setek[g] + " " + nazwy_jednosci[j]
        print(a)
    elif d == 1:
        z = nazwy_setek[g] + " " + nazwy_nast[liczba]
        print (z)
    else:
        koniec = nazwy_setek[g] + " " + nazwy_dziesiatek[d] + " " + nazwy_jednosci[j]
        print (koniec)


#----------------------------------------------------------------------


{x: str(x) for x in range(10)}

#-------------------------------------------------------------------------------------------------

slownik_sam =  {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

[x for x in slownik_sam.keys() if slownik_sam[x] >5000]

#-------------------------------------------------------------------------------------------------

#funkcje

def funkcja1 ():
    print ("Jestem Funkcja1")


def funkcja2 ():
    print ("Jestem Funkcja2")


def funkcja_spojna ():
    list_moja = {1: funkcja1, 2: funkcja2}
    miara = int(input("wpisz 1 albo 2"))
    return list_moja[miara]

f = funkcja_spojna()
f()
