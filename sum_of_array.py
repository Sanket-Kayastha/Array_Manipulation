import math

def sum_of_array(arr):
    total = 0
    for element in arr:
        total += element

    return total

arr = [2,5,6,8,6]

sum = sum_of_array(arr)
print(f"Sum of array is {sum}")

# print(sum(arr))

