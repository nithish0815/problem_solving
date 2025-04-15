def find_max(arr):
    max_val = arr[0]
    for num in arr:

        if num > max_val:
            max_val = num
    return  max_val

arr = [3, 5, 0, 6, 1, 2, 4]
print(find_max(arr))