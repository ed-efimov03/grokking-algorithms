def max_number(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0] 
        else:
            return arr[1] 
    sub_max_number = max_number(arr[1:])
    if arr[0] > sub_max_number:
        return arr[0]
    else:
        return sub_max_number
    
print(max_number([3, 5, 7, 6]))