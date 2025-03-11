# Write a Python program to search a specific value from a given list of values using binary search method.

def bs(list1, num):
    low = 0
    high = len(list1) - 1
    mid = 0
    while low <= high :
        mid = (high + low) // 2
        if list1[mid] < num:
            low = mid + 1
        elif list1[mid] > num:
            high = mid - 1
        else:
            return mid+1
        
x = int(input("Enter number of element you want to enter: "))
list1 = []
for i in range(x):
    y = int(input("Enter element: "))
    list1.append(y)
list1.sort()
print("Sorted list is: ", list1)
num = int(input("Enter number to search: "))
print(f"Index of entered number is {bs(list1,num)}")