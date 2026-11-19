class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        temp = 0
        for i in range(n//2):
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
        return arr

arr = [1,2,3,4,5]
sol = Solution()
sol.reverseArray(arr)
print(arr)