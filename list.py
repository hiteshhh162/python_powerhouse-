# create  a list of number , then calculate and prin the sum and average 

# lists =[1,2,3,4,5,6,7,8,9,0]
# sum =0
# for i in lists:
#     sum+=i

# l = len(lists)

# print ("sum is :",sum)
# print("Average is :",sum /l)

#Q2 find the largest  element in the list along with its position (index)

# l = [ 10,20,30,40,40]
# max =0
# ind=0
# for i in range(len(l)):
#     if max < l[i]:
#         ind = i
#         max= l[i]

# print(f"Their index position is :{ind} nad maximum value is :{max} ")        


#Q3 identify the second largest element in the list withoutsorting directly 


# l = [ 10,20,30,40,40]
# max =0
# second=0
# ind=0
# for i in range(len(l)):
#     if max < l[i]:
#         ind = i
#         second=max
#         max= l[i]


# print(f"Second largest number is :{second}")


#Q4 verify whether the list element are in ascending order 

# l = [1,2,9,4,5]

# check = 0

# for i in range (len (l)-1):
#     if l[i] > l[i+1]:
#         print("Your list is not sorted in ascending order ")
#         break
# else :
#     print("Your list is sorted in ascending order ")    


#Q5 Shift all element one position tothe lest  , with the first element moving to the end 

# l=[1,2,3,4,5,6,7,8,9,0]
# temp=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[i+1]=temp

# print(l)


#Q6 generalize the previous problem rotete the list k times to the left

# l=[1,2,3,4,5,6,7,8,9,0]
# temp=l[0]
# k = int(input("Enter k for you want to move element :"))
# while k >0:
#     for i in range(len(l)-1):
#         l[i],l[i+1]=l[i+1],l[i]
#     k-=1

# print(l)


#Q7 reverse the entire list without using extra space (i.e.,swap element )


l=[1,2,3,4,5,6,7,8,9,0]
b = len(l)-1
for i in range(len(l)//2):
        l[i],l[b]=l[b],l[i]
        b-=1
print(l)


