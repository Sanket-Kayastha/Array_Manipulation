def monotonic_array(arr):
    increasing = decreasing = True
    n = len(arr)
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            decreasing =False
        elif arr[i] < arr[i-1]:
            increasing = False

    return increasing or decreasing



arr1 = [1,2,2,3]
arr2= [1,4,5,2]
arr3 = [4,3,2,1]

result1 = monotonic_array(arr1)
result2 = monotonic_array(arr2)
result3 = monotonic_array(arr3)
print("arr1 is : ", result1)
print("arr2 is : ",result2)
print(f"arr3 is : {result3}")