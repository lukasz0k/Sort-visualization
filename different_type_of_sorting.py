"""Write function to sort input list, don't use sort"""

from random import randint as ri        #import one feature to create a random list

def createList(n):                      #random list creating function
    mylist = []
    for i in range(n):
        mylist.append(ri(0,1000))
    return mylist

"""Bubble sort"""
"""Simplest algorithm that compares the list items"""
"""Take one argument and compare with the next one"""
"""Computional complexity: O(n^2)"""
"""Memory complexity: O(1)"""

def bubble(mylist):
    n = len(mylist)
    while n > 1:
        change = False
        for i in range(0, n-1):
            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                change = True
        n -= 1
        if change == False:
            break
    return mylist

"""Insert sort"""
"""Like stacking card, take one and look for lesser or equal then"""
"""Computional complexity: O(n^2)"""
"""Memory complexity: O(1)"""

def insert(mylist):
    n = len(mylist)
    for i in range(1,n):
        current = mylist[i]
        previous = i-1
        while previous >= 0 and current < mylist[previous]:
            mylist[previous + 1] = mylist[previous]
            previous -= 1
        mylist[previous + 1] = current
    return mylist

"""Merge sort"""
"""Recursive algorithm"""
"""Split main list, sort smaller and connect them"""
"""Computional complexity: O(n logn)"""
"""Memory complexity: O(n)"""

def merge(myList, first, center, last):
    x, y = first, center+1
    tmp = []
    while x <= center and y <= last:
        if myList[y] < myList[x]:
            tmp.append(myList[y])
            y += 1
        else:
            tmp.append(myList[x])
            x += 1
    if x <= center:
        while x <= center:
            tmp.append(myList[x])
            x += 1
    else:
        while y <= last:
            tmp.append(myList[y])
            y += 1
    s = last - first + 1
    i = 0
    while i < s:
        myList[first + i] = tmp[i]
        i += 1
    return myList

def mergeSort(lista, first, last):
    if first != last:
        center = (first + last) // 2
        mergeSort(lista, first, center)
        mergeSort(lista, center + 1, last)
        merge(lista, first, center, last)
    return lista

"""Selection Sort"""
"""Lokk for the smallest value and make it a first one, delete value"""
"""Repeat for the list minus previous smallest values"""
"""Computional complexity: O(n^2)"""
"""Memory complexity: O(1)"""

def selection(myList):

    for i in range(0, len(myList)):
        min = i
        for j in range(i + 1, len(myList)):
            if myList[min] > myList[j]:
                min = j

        if i != min:
            myList[i], myList[min] = myList[min], myList[i]
    return(myList)

"""Quick Sort"""
"""Recursive algorithm"""
"""Create a pivot and divite main list into two smallest, lesser and greater them pivot"""
"""Repeat for new lists"""
"""Computional complexity: O(n logn)"""

def quick(myList):
    if len(myList) <= 1:
        return myList

    pivot = myList[0]
    mniej = []
    wiecej = []
    eq = []

    for i in myList:
        if i > pivot:
            wiecej.append(i)
        if i < pivot:
            mniej.append(i)
        if i == pivot:
            eq.append(i)

    return quick(mniej) + eq + quick(wiecej)

myList = createList(20)
print(bubble(myList))
print(insert(myList))
print(mergeSort(myList, 0, len(myList)-1))
print(selection(myList))
print(quick(myList))