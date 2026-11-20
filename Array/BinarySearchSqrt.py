def search_sqrt(n):
    st = 1
    end = n
    res = 1
    
    while st <= end:
        mid = end + (st - end) // 2
        
        if mid*mid<=n:
            res = mid
            st = mid+1
        else: end = mid-1
    return res
num = 55
sqrt = search_sqrt(num)
print(sqrt)
