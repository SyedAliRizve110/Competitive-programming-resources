# *
# * *
# * * *
# * * * *
rows = 5
for i in range(1,rows):
    for j in range(0,i):
        print('* ', end="") 
    print()
    
rows = 5
for i in range(1,rows):
    print('* '*i) #using string multiplication '* ' *3 = * * *
print()