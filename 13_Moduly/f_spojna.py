
# funkcje
import sys
def funkcja1():
    print("Jestem Funkcja1")


def funkcja2():
    print("Jestem Funkcja2")


def funkcja_spojna(n):
    list_moja = {1: funkcja1, 2: funkcja2}
    miara = int(input("wpisz 1 albo 2"))
    return list_moja[miara]


f = funkcja_spojna()
f()

if __name__= '__main__':

    print(sys.argv)