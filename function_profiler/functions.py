from decorators import measure_time, measure_memory
import os
import random

@measure_time
@measure_memory
def bubble_sort(arr):
    """Sortowanie bąbelkowe O(n^2)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@measure_time
@measure_memory
def quick_sort(arr):
    """Prosty quicksort z pivotem na początku"""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

@measure_time
@measure_memory
def quick_sort(arr):
    """In-place quicksort z losowym pivotem"""
    def partition(a, lo, hi):
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    def _qs(a, lo, hi):
        if lo < hi:
            pivot_index = random.randint(lo, hi)
            a[pivot_index], a[hi] = a[hi], a[pivot_index]
            p = partition(a, lo, hi)
            _qs(a, lo, p - 1)
            _qs(a, p + 1, hi)

    _qs(arr, 0, len(arr) - 1)
    return arr

@measure_time
@measure_memory
def builtin_sort(arr):
    """Sortowanie wbudowane w Pythonie (Timsort)"""
    return sorted(arr)

@measure_time
@measure_memory
def read_large_file():
    """Test I/O: zapisz i wczytaj duży plik tekstowy"""
    filename = "testfile.txt"
    with open(filename, "w") as f:
        f.writelines("Some line of text\n" * 1000000)
    with open(filename, "r") as f:
        lines = f.readlines()
    os.remove(filename)
    return lines