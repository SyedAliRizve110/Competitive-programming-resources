class BinarySearch:
    def binarySearch(self, arr: list[int], k: int) -> int:
        # code
        start = 0
        end = len(arr)-1
        while start <= end:
            mid = end + (start - end) //2
            
            if arr[mid] == k:
                return mid
            if arr[mid] > k:
                end = mid-1
            else: start = mid +1
        return -1
arr = [1,2,4,5,6,7,8,11,14,33,34,46,54,67,76,99]
k = 3
search = BinarySearch()
num = search.binarySearch(arr, k)
print(num)
