from random import randrange
import time

# -------------- Bubble sort --------------
#def bubble(lst):
#    if len(lst) > 1:
#        for _ in range(len(lst)):
#            for i, val in enumerate(lst):
#                if i == len(lst) - 1:
#                    break
#                elif lst[i] > lst[i + 1]:
#                    lst[i] = lst[i + 1]
#                    lst[i + 1] = val
#    return lst


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
        mid = (lowerBound + upperBound) // 2

        if lst[mid] == value:
            return mid + 1
        elif lst[mid] < value:
            lowerBound = mid + 1
        else:
            upperBound = mid - 1
    return lowerBound


# -------------- Mergesort ---------------
def mergesort(lst):
    k = 4  # Max lenght of elements in sublists
    if len(lst) > 1:
        sublsts = [
            lst[i * k:(i + 1) * k]
            for i in range((len(lst) + k - 1) // k)
        ]

        for i in range(0, len(sublsts)):  # o(n)
            #asort(sublsts[i])   # Uncomment to use linear sort
            bsort(sublsts[i])

        temp = []
        while len(sublsts) > 1:
            for i in range(0, len(sublsts), 2):                     #O(n/2)       
                if i * 2 + 1 > len(sublsts):                        #O(1)
                    temp.append(sublsts[i])                         #O(n)
                else:
                    temp.append(merge(sublsts[i], sublsts[i + 1]))  #O(n)
            sublsts = temp
            temp = []
        return sublsts


def merge(L, R):
    newarray = []
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            newarray.append(L[i])  # append placeholder swap to k to use constant o(1)
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
a = [randrange(10) for i in range(20)]
# a = [0, 7, 3, 1, 3, 8, 1, 0, 8, 0]
#a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print("\nList:          ", a)
# print("* Bubble sort: ", bubble(a))
# print("* Linear sort: ", asort(a))
# print("* Binary sort: ", bsort(a))
# print("* Merge sort (bsort): ", mergesort_bsort(a))

start = time.time()

mergesort(a)

end = time.time()
final_time = end - start

print(mergesort(a))
print("execution time :", final_time)
