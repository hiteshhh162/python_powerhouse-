# create  a list of number , then calculate and prin the sum and average 

# lists =[1,2,3,4,5,6,7,8,9,0]
# sum =0
# for i in lists:
#     sum+=i

# l = len(lists)

# print ("sum is :",sum)
# print("Average is :",sum /l)

#Q2 find the largest  element in the list along with its position (index)

l = [ 10,20,30,40,40]
max =0
ind=0
for i in range(len(l)):
    if max < l[i]:
        ind = i
        max= l[i]

print(f"Their index position is :{ind} nad maximum value is :{max} ")        
