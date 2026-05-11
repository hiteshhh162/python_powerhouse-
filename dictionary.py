# # Q1 display all distinct element present in the given array
# a= [ 1,1,1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,7,7,8,8,9,9,9,7,7]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d.keys())        


# #Q2 count how many time each element apears using a dictionary or hash map 
# a= [ 1,1,1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,7,7,8,8,9,9,9,7,7]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# Q3 jewels and stones , count how many stones are also jewels based on given strings .

# jewels =["hello"]
# stones=["hEllojay"]

# d = {}
# for i in stones:
#     if i in d.keys():
#         d[i] +=1
#     else :
#         d[i]=1    
# count =0        
# for i in d.keys():
#     if i in jewels:
#         count +=1

# print(count)        


# Q4 verify if a sentencee conain every letter of the english alphabets at least once 

# sentence = "abcdefghijklmnopqrstuvwxyz"
# d= {}
# for i in sentence:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1 

# if len(d.keys()) == 26 :
#     print (True)
# else:
#     print(False)

# #Q5 find the frist character that appears twice in a string 
# sentences = "hello i am hitesh jadav "
# d = {}
# for i in sentences:
#     if i in d.keys():
#         d[i]+=1
#         print(i)
#         break
#     else:
#         d[i]=1


# Q6 retrun the sum of element that appears exactly once in the array

# nums = [ 1,2,3,4,5]

# d ={}
# count = 0
# for i in nums:
#     if i in d.keys():
#         d[i]+=1
#         if d[i] > 2:
#             continue
#         count -=1
#     else:
#         d[i]=1
#         count +=1

# print(count)        


#Q7 sort names of people based on their height in descending order 

# name = ["hitesh" ,"aakash","vipul"]
# height = [180,160,162]
# d={}
# for i in range(len(name)):
#     d[height[i]]=name[i]

# d=sorted (d.items() , key=lambda x:x[0] , reverse = True)

# for i in range (len(d)):
#     names[i] = d[i][1]

# print(names)    

# Q8 compare character frequency of two sting and check if they  match

# str1= "hiteshjadaa"
# str2="jadavhitesh"

# if len(str1)==len(str2):
#     d = {}
#     for i in str1:
#         if i in d.keys():
#             d[i]+=1
#         else :
#             d[i]=1

#     for i in str2:
#         if i in d.keys():
#             d[i]-=1
#         else:
#             print("Extra value are add")
#             break

#     for i in d:
#         if d[i] != 0:
#             print("not same")
#             break                    
#     else:
#         print("Your string are same")

# else:
#     print("not same")        
# 
# 
# Detect and print element that appear more than once in the array 
nums = [1,1,2,3,4,2,23,3,425,34,645,6456,2,52,534,5,6]
d={}

for i in nums:
    if i in d.keys():
        d[i]+=1

    else:
        d[i]=1

for i in d:
    if d[i] > 1:
        print(f"{i}  {d[i]}")
        