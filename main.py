#Code by AryanNaik24 on github

import random
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation



# Sorting generator functions for visualization
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr[:]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr[:]
    return i + 1

def merge_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort(arr, left, mid)
        yield from merge_sort(arr, mid + 1, right)
        yield from merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    temp = arr[:]
    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if temp[i] < temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1
        yield arr[:]
    while i <= mid:
        arr[k] = temp[i]
        i += 1
        k += 1
        yield arr[:]
    while j <= right:
        arr[k] = temp[j]
        j += 1
        k += 1
        yield arr[:]


array_size = 50
array = [random.randint(1, 100) for _ in range(array_size)]
sorting_algorithm = quick_sort

fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(array)), array, align="edge")
ax.set_xlim(0, array_size)
ax.set_ylim(0, max(array) + 10)
ax.set_title("Sorting Algorithm Visualization")

def update(arr):
    for rect, val in zip(bar_rects, arr):
        rect.set_height(val)

def animate(frame):
    try:
        new_arr = next(sort_generator)
        update(new_arr)
    except StopIteration:
        return

# Start sorting and animation
sort_generator = sorting_algorithm(array)
ani = FuncAnimation(fig, animate, interval=50)
plt.show()

