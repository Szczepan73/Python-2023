
# funkcje
import sys
def funkcja1():
    return "Jestem Funkcja1"


def funkcja2():
    return "Jestem Funkcja2"

list_moja = {'1': funkcja1, '2': funkcja2}
def funkcja_spojna(n):
#    miara = int(input("wpisz 1 albo 2"))
    miara = sys.argv[1]
    return list_moja[miara]


#
if __name__ == '__main__':
    print(sys.argv)
    klucz = (sys.argv[1])
    print (klucz)
    print (list_moja[klucz]())

#d = funkcja_spojna()
#print (d)
