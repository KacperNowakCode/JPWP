from decorators import measure_time

def _merge_sort_v1_recursive_core(arr):
    """Core logic: Rekurencyjny Merge Sort (out-of-place), bez dekoratorów."""

    def _merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = _merge_sort_v1_recursive_core(left_half)
    right_half = _merge_sort_v1_recursive_core(right_half)

    return _merge(left_half, right_half)

@measure_time
def merge_sort_v1_recursive(arr):
    """Rekurencyjny Merge Sort (out-of-place), opakowany do profilowania."""
    arr_copy = list(arr)
    return _merge_sort_v1_recursive_core(arr_copy)


def _merge_sort_v2_iterative_core(arr):
    """Core logic: Iteracyjny Merge Sort (out-of-place z pomocniczą tablicą), bez dekoratorów."""

    def _merge_transfer(src, dest, start, mid, end):
        i = start
        j = mid + 1
        for k in range(start, end + 1):
            if i > mid:
                dest[k] = src[j]
                j += 1
            elif j > end:
                dest[k] = src[i]
                i += 1
            elif src[i] <= src[j]:
                dest[k] = src[i]
                i += 1
            else:
                dest[k] = src[j]
                j += 1

    n = len(arr)
    if n <= 1:
        return list(arr)

    src = list(arr)
    dest = [0] * n

    current_size = 1
    while current_size < n:
        left_start = 0
        while left_start < n - current_size:
            mid = left_start + current_size - 1
            right_end = min(left_start + 2 * current_size - 1, n - 1)
            _merge_transfer(src, dest, left_start, mid, right_end)
            left_start += 2 * current_size
        src, dest = dest, src
        current_size *= 2

    return src

@measure_time
def merge_sort_v2_iterative(arr):
    """Iteracyjny Merge Sort (out-of-place z pomocniczą tablicą), opakowany do profilowania."""
    arr_copy = list(arr)
    return _merge_sort_v2_iterative_core(arr_copy)


@measure_time
def builtin_sort(arr):
    """Wbudowane sortowanie Pythona jako punkt odniesienia (Timsort)"""
    return sorted(arr)