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

# def dzielnik(a):
#     div = []
#     for i in range(1, a+1):
#         if a % i ==0:
#             div.append(i)
#     print(div)
# dzielnik(8)


# # sortowanie przez wstawianie O(n^2)
# import random
# import time

# def wstaw(tab):
#     for i in range(1, len(tab)):
#         siu = tab[i]
#         j = i-1
#         while j>=0 and siu < tab[j]:
#             tab[j+1] = tab[j]
#             j -= 1
#         tab[j+1] = siu

# # przyklad
               
# tab = [8,4,6,5,9]
# wstaw(tab)
# print(tab)
# ile = 100
# tab = [random.randint(1,ile) for _ in range(ile)]
# start_time = time.time()
# wstaw(tab)
# end_time = time.time()
# print("Czas wykonania sortowania to: ", end_time - start_time)


# sortowanie dziel i rządź
tab1 = [1,3,5,7]
tab2 = [2,4,6,8]
def sortownia(arr1, arr2):
    arr = arr1 + arr2
    print(arr.sort())
sortownia(tab1, tab2)