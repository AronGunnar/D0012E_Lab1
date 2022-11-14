import math
import array
from random import randrange


# -------------- Bubble sort --------------
def bubble(lst):
    if len(lst) > 1:
        for _ in range(len(lst)):
            for i, val in enumerate(lst):
                if i == len(lst) - 1:
                    break
                elif lst[i] > lst[i + 1]:
                    lst[i] = lst[i + 1]
                    lst[i + 1] = val
    return lst


# ----- Insertionsort (linear search) -----
def asort(lst):
    for j, val in enumerate(lst):
        i = j - 1
        while i >= 0 and lst[i] > val:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = val
    return lst


# ----- Insertionsort (binary search) -----
def bsort(lst):
    for i, val in enumerate(lst):
        located = bsearch(val, 0, i - 1, lst)

        j = i - 1
        while j >= located:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = val
    return lst


def bsearch(value, lowerBound, upperBound, lst):
    while lowerBound <= upperBound:
        mid = math.floor((lowerBound + upperBound) / 2)

        if lst[mid] == value:
            return mid + 1
        elif lst[mid] < value:
            lowerBound = mid + 1
        else:
            upperBound = mid - 1
    return lowerBound


# -------------- Mergesort ---------------
def mergeKlists(lst):
    k = 4                       #Max lenght of elements in sublists
    if len(lst) > 1:
        array = [
                lst[i * 4:(i + 1) * k] 
                for i in range((len(lst) + k - 1) // k )
                ]
        
        for i in range(0, len(array)): #o(n)
            bsort(array[i])

        
        a = [0 for i in range(len(array))] #o(n)
        
        print(array)

        amount = len(array)
        interval = 1
        newarray = []
        while interval < amount:
            for i in range(0, amount - interval, interval*2):
                if interval+1 >= len(array):
                    newarray.append(array[i])
                    continue
                else:
                    newarray.append(merge2lists(array[i], array[i + interval]))
                interval *= 2
        return newarray

def merge2lists(L, R):
    newarray = []
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            newarray.append(L[i])       #append placeholder swap to k to use constant o(1)
            i += 1
        else:
            newarray.append(R[j])
            j += 1
        k += 1
    
    while i < len(L):
        newarray.append(L[i])
        i += 1
        k += 1
 
    while j < len(R):
        newarray.append(R[j])
        j += 1
        k += 1
    
    return newarray


    


# --------------- Run/Test ---------------
# test = [0, 1, 2, 4, 3, 5, 6]
a = [randrange(10) for i in range(20)]
# a = [0, 7, 3, 1, 3, 8, 1, 0, 8, 0]

print("\nList:          ", a)
#print("* Bubble sort: ", bubble(a))
#print("* Linear sort: ", asort(a))
#print("* Binary sort: ", bsort(a))
#print("* Merge sort (bsort): ", mergesort_bsort(a))
print(mergeKlists(a))