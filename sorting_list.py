import timeit
import random

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Вимірюємо час виконання для кожного алгоритму на випадковому наборі даних
random_data = [random.randint(0, 1000) for _ in range(1000)]

merge_sort_time = timeit.timeit(lambda: merge_sort(random_data.copy()), number=10)
insertion_sort_time = timeit.timeit(lambda: insertion_sort(random_data.copy()), number=10)
timsort_time = timeit.timeit(lambda: sorted(random_data.copy()), number=10)

print("Merge Sort час виконання:", merge_sort_time)
print("Insertion Sort час виконання:", insertion_sort_time)
print("Timsort час виконання:", timsort_time)
