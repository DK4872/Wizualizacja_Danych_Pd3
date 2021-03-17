print("Zadanie 1")
a = [x - 1 for x in range(1, 11)]
print(a)
b = [4 ** x for x in range(8)]
print(b)
c = [x for x in b if x % 2 == 0]
print(c)
print("Zadanie 2")
liczby = [1, 5, 9, 12, 24, 53, 11, 33, 18, 62]
lista1 = []
for i in liczby:
    if i % 2 == 0:
        lista1.append(i)
print("Liczby parzyste:")
print(lista1)
print("Zadanie 3")
slownik = {"Chlebek": "sztuki", "Ziemniaki": "kilogramy", "Sałata": "sztuki",
           "Pomidory": "kilogramy"}
sztukowe = [produkt for produkt in slownik.keys() if slownik[produkt] == "sztuki"]
print(sztukowe)
print("Zadanie 4")


def sprawdzacz(a0, b0, c0):
    suma = a0 ** 2 + b0 ** 2
    if c0 ** 2 == suma:
        print("To jest trójkąt prostokątny")
    else:
        print("To nie jest trójkąt prostokątny")


print(sprawdzacz(3, 4, 5))
print("Zadanie 5")


def pole_trapezu(x1=1, x2=2, h1=3):
    return ((x1 + x2) * h1) / 2


print(pole_trapezu())
print("Zadanie 6")
# def iloczyn(a1=1,b=4,ile=10):
# print(iloczyn())
# nie jestem pewien co dalej
print("Zadanie 7")


def funkcja(*elementy):
    if len(elementy) != 0:
        x1 = 1
        for x in range(len(elementy)):
            x1 *= elementy[x]
        return x1
    else:
        return 0


print(funkcja(1, 2, 3, 4, 5, 6))
print("Zadanie 8")


def zakupy(**prod):
    items = len(prod)
    if items != 0:
        suma = 0
        ceny = [cena for cena in prod.values() if isinstance(cena, float) is True or isinstance(cena, int) is True]
        print(ceny)
        for x in range(len(ceny)):
            suma += float(ceny[x])
    else:
        return "Brak zakupów"
    return suma


print(zakupy(czekolada=3, woda=1, chlebek=2))
print("Zadanie 9")
# import ciagi
# from ciagi import *
