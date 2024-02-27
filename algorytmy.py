# #cwiczenie: napisz pseudokod algorytmu, a następnie przeksztalc go w kod Pythona, ktory sortuje liste liczb metoda babelkowa
# #wejscie: tablica (array)
# #wyjscie: tablica (array)

# tab = [2,5,8,1, 4, 3, 1,6,6,9]
# n = len(tab)
# def sortujBabelkowo(tab, n):
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if tab[j] > tab[j+1]:
#                 tab[j] , tab[j+1] = tab[j+1] , tab[j]
            
#     print(tab)
# sortujBabelkowo(tab, n)


# #cwiczenie: kod Pythona kod euklidesa
# #wejscie: 2 liczby
# #wyjscie: 1 liczba
# #1
# def euklides(a, b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     print(a)

# euklides(48, 12)

# #2
# def euk(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# print(euk(48,12))

#cwiczenie: znajdowanie dzielnikow
#funkcja, ktora przyjmuje liczbe calkowita jako argument i zwraca liste wszystkich jej dzielnikow
#wejscie: 1 liczba calkowita
#wyjscie: lista/tablica

def dzielnik(a):
    div = []
    for i in range(1, a+1):
        if a % i ==0:
            div.append(i)
    print(div)
dzielnik(8)