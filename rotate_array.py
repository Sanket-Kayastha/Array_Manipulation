def rotate_array(arr,d):
    n = len(arr)
    if d<0 or d>n:
        return "Rotation Not Possible"
    
    rotate_array = [0]*n
    for i in range(n):
        rotate_array[i] = arr[(i+d)%n]

    return rotate_array



arr = [1,2,3,4,5]
d = 4

result = rotate_array(arr,d)
print(result)