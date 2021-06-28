"""Compare time of different type of sorting"""
"""This program create a records for analyze sort methods"""
"""Create a few new list with results and seve it into .txt file"""

import timeit
from different_type_of_sorting import *           #import all functions from file different_type_of s

# print(f'Bubble sort: {timeit.timeit("bubble(createList(10))", globals=locals())} s\n'
#       f'Insert sort: {timeit.timeit("insert(createList(10))", globals=locals())} s\n'
#       f'Merge sort: {timeit.timeit("mergeSort(createList(10), 0, len(createList(10))-1)", globals=locals())} s\n'
#       f'Selection sort: {timeit.timeit("selection(createList(10))", globals=locals())} s\n'
#       f'Quick sort: {timeit.timeit("quick(createList(10))", globals=locals())} s')

# print(f'Bubble sort: {timeit.timeit("bubble(createList(100))", globals=locals())} s\n'
#       f'Insert sort: {timeit.timeit("insert(createList(100))", globals=locals())} s\n'
#       f'Merge sort: {timeit.timeit("mergeSort(createList(100), 0, len(createList(100))-1)", globals=locals())} s\n'
#       f'Selection sort: {timeit.timeit("selection(createList(100))", globals=locals())} s\n'
#       f'Quick sort: {timeit.timeit("quick(createList(100))", globals=locals())} s')

filepath = "times.txt"
f = open(filepath, "w")

elements = [1, 2, 5, 10, 20, 40, 70, 100, 150, 200, 270, 350, 450, 550, 700]

for n in elements:
    f.write(f'{str(timeit.timeit(f"bubble(createList({n}))", globals=locals()))} ')
    f.write(f'{str(timeit.timeit(f"insert(createList({n}))", globals=locals()))} ')
    f.write(f'{str(timeit.timeit(f"mergeSort(createList({n}), 0, len(createList({n}))-1)", globals=locals()))} ')
    f.write(f'{str(timeit.timeit(f"selection(createList({n}))", globals=locals()))} ')
    f.write(f'{str(timeit.timeit("quick(createList(100))", globals=locals()))} ')
    f.write(f'{n}\n')

f.close()
