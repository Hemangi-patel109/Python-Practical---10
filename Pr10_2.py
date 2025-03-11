# Write a python program to sort the elements of list values using selection sort.

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  

values = [64, 25, 12, 22, 11]
print("Original list:", values)
selection_sort(values)
print("Sorted list:", values)