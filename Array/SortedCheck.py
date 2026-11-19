class Solution:
    def check_sort(self, arr):
            n = len(arr)
            i =1
            while i < n-1:
                if arr[i] > arr[i+1]:
                    return False
                i+=1
            return True

arr = [50,60,55,80,89,99]
sol = Solution()
isSort = sol.check_sort(arr)
print(isSort)