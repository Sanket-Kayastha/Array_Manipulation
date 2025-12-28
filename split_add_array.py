def split_add(arr,k):
    n = len(arr)
    if k<0 or k>n:
        return f"Correct the array {arr} or k vaue {k}"
    
    first_part = arr[:k]
    second_part = arr[k:]
    return second_part+first_part



arr = [1,2,3,4,5,6]
k=4
result = split_add(arr, k)
print(result)