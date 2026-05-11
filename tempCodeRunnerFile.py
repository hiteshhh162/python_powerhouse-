l = [1,2,3,4,5]

check = 0

for i in range (len (l)-1):
    if l[i] > l[i+1]:
        print("Your list is not sorted in ascending order ")
        break
else :
    print("Your list is sorted in ascending order ")    
