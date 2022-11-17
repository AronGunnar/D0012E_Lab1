from random import randrange
import cProfile
import time


# -------------- Bubble sort --------------
# def bubble(lst):
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
    for j, val in enumerate(lst):  # n-1
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


# Insertionsort: Binary search
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
def mergesort(lst, k):
    # k = 4  # Max lenght of elements in sublists
    if len(lst) > 1:
        sublsts = k_elem_sublists(lst, k)  # Uncomment for
        # sublsts = one_elem_sublists(lst)

        temp = []
        while len(sublsts) > 1:  # ciel(n/2k) + 1
            for i in range(0, len(sublsts), 2):  # n/2k + 1
                if len(sublsts) - 2 * len(temp) > 1:  # O(1)
                    temp.append(merge(sublsts[i], sublsts[i + 1]))  # O(1)
                else:
                    temp.append(sublsts[i])  # O(1)
            sublsts = temp
            temp = []
        return sublsts[0]
    return lst


# Mergesort: Merge sublists
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


# Mergesort: Divide into sublists (k or one)
def k_elem_sublists(lst, k):
    sublsts = [
        lst[i * k:(i + 1) * k]
        for i in range((len(lst) + k - 1) // k)
    ]

    for i in range(0, len(sublsts)):  # o(n)
        # asort(sublsts[i])   # Uncomment to use linear sort
        bsort(sublsts[i])
    return sublsts


def one_elem_sublists(lst):
    temp = []
    for i, val in enumerate(lst):
        temp.append([val])
    lst = temp

    return lst


# --------------- Run/Test ---------------
a = [randrange(10) for i in range(1000)]


# sorted_list = list(range(0, 10000))
# revered_list = sorted_list.copy()
# revered_list.reverse()


def test1(length):
    besttime = 100
    temptime = 0
    k = 2
    best_k = k
    accuracy = 50  # Amount of random lists tested
    while k < length / 2 - 1:
        for i in range(accuracy):
            lst = [randrange(10) for i in range(1000)]

            start_time = time.time()
            mergesort(lst, k)
            endtime = time.time()

            temptime += endtime - start_time

        temptime /= accuracy
        if temptime < besttime:
            besttime = temptime
            best_k = k
            print("Time: ", besttime, "| k :", best_k)
        else:
            print("Running! ", "( k =", k, ")")

        k += 1

        if abs(k - best_k) > 30:
            break

    print("Best time: ", besttime, "| Best k :", best_k)


test1(len(a))


# cProfile.run("mergesort(a)")
# print(lst)
# print(mergesort(lst))
# cProfile.run("mergesort_bsort(revered_list, k)")
# print(lst)
# print(mergesort_bsort(lst))
# cProfile.run("mergesort_asort(revered_list)")


# print(lst)
# print(mergesort_asort(lst))
# cProfile.run("asort(a)")
# cProfile.run("bsort(a)")

# test(revered_list)
