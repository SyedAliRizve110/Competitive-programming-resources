def reverseArray(arr): # two pointer approch
    left, right = 0, len(arr)-1
    while left<right:
        arr[left],arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [5,10,15,20,25,30]
reverseArray(arr)
print(arr)