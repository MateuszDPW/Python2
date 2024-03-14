data = [{'id': 1, 'value':5},
        {'id': 2, 'value':3},
        {'id': 3, 'value':5},
        {'id': 4, 'value':8},
        {'id': 5, 'value':3}]

# zastosowac sortowanie niestabilne (quicksort)

def quicksort_dicts(arr, key='value'):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x[key] <= pivot[key]]
    greater = [x for x in arr[1:] if x[key] > pivot[key]]
    return quicksort_dicts(lesser, key)+[pivot]+quicksort_dicts(greater, key)

print(quicksort_dicts(data))

# zastosowac sortowanie stabilne (przez scalanie)




# # to samo tylko że z pomocą
# data = [{'id': 1, 'value':5},
#         {'id': 2, 'value':3},
#         {'id': 3, 'value':5},
#         {'id': 4, 'value':8},
#         {'id': 5, 'value':3}]

# # zastosowac sortowanie niestabilne (quicksort)
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x['value'] < pivot['value']]
#     middle = [x for x in arr if x['value'] == pivot['value']] 
#     right = [x for x in arr if x['value'] > pivot['value']]
#     return quick_sort(left) + middle + quick_sort(right)

# print(quick_sort(data))

# # zastosowac sortowanie stabilne (przez scalanie)
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

# print(merge_sort(data))
