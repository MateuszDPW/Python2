# #cwiczenie: napisz pseudokod algorytmu, a następnie przeksztalc go w kod Pythona, ktory sortuje liste liczb metoda babelkowa
# #wejscie: tablica (array)
# #wyjscie: tablica (array)

# tab = [2,5,8,1,4,3,1,6,6,9]
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
#         key = tab[i]
#         j = i-1
#         while j>=0 and key < tab[j]:
#             tab[j+1] = tab[j]
#             j -= 1
#         tab[j+1] = key

# # przyklad
               
# tab = [8,4,6,5,9]
# wstaw(tab)
# print(tab)
# ile = 100
# tab = [random.randint(1,ile) for _ in range(ile)]
# start_time = time.time()
# wstaw(tab)
# end_time = time.time()
# print("Czas wykonania sortowania dla zbioru ",ile," to: ", end_time - start_time)


# # sortowanie dziel i rządź
# tab1 = [1,3,5,7]
# tab2 = [2,4,6,8]
# def sortownia(arr1, arr2):
#     arr = arr1 + arr2
#     print(arr.sort())
# sortownia(tab1, tab2)

# # sortowanie szybkie

# def quicksort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot = arr[0]
#     lesser = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]
#     return quicksort(lesser)+[pivot]+quicksort(greater)

# print(quicksort([3,6,7,8,3,4,1]))

# import random

# def median(arr):
#     return sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]

# def quicksort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot = median(arr)

#     lesser = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]
#     return quicksort(lesser)+[pivot]+quicksort(greater)

# print(quicksort([3,6,7,8,3,4,1]))

# sortowanie przez scalanie
# def merge_sort(arr):    
#     if len(arr) <= 1    :      # base case
#         return arr           
#     else               :               # recursive case
#         mid   = len(arr)//2       # find the mid point
#         left  = merge_sort(arr[:mid])   # split array into two halves
#         right = merge_sort(arr[mid:])   # do the same on the other half
#         res = []              # create a new list to hold the merged result
        
#         i=j=0                     # set pointers for the lists
#         while i < len(left) and j < len(right):
#             if left[i]['value'] <= right[j]['value']:   
#                 res.append(left[i])   # append the smaller one to the sorted part of the final list
#                 i += 1             # move the pointer in the left list
#             else:
#                 res.append(right[j])  # append the larger one directly to the final list
#                 j += 1              # move the pointer in the right list
#         # add all remaining elements from both lists to the final list
#         res += left[i:]
#         res += right[j:]
#         return res
# print(merge_sort([3,6,7,8,3,4,1]))
