num = 1234
sum = 0
if num >=0:
    while (num>0):
        sum = sum * 10 + num%10
        num = num // 10
print(sum)
    