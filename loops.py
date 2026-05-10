# print 10 time  "Hello world !"

# for i in range (1,11,1):
#     print("Hello world !")


#Q2 print number from 10 to 40 

# for i in range (10, 41 ,1):
#     print(i)

#Q3 print number from -10 to 20 

# for i in range (-10 ,21 ,1):
#     print(i) 

#Q4 print number from 34 to 5 

# for  i in range (34,4,-1):
#     print(i)

# Q5 print table of given user number 

# num = int(input("Enter number for table :"))

# for i in range (1,11,1):
#     print(f"{num} * {i} = {num*i} ")


# for i in range(10):
#     print(i)



#Q6 Display number in increasing order from 1 up to  a given  number n.
# n = int (input ("Enter a number to print 1 to n number :"))

# for i in range (1,n+1,1):
#     print(i)



#Q7 display number  in decreasing order from n to 1 .

# n = int (input ("Enter a number to print n to 1 number :"))

# for i in range(n,0,-1):
#     print(i)

#Q8 take input n and calculate the total sum from 1 to n 

# n = int(input ("Enter n number to  sum  from 1 to n :")) 
# sum =0 
# for i in range(n+1):
#     sum+=i

# print(f"Total sum is from 1 to {n} is : {sum}")     



#Q9 calculate the factorial (n!) using a loop  - multiplying number from 1 to n ,

# n = int (input("Enter a number you want to find this factorial :"))
# fac=1
# for i in range (1,n+1,1):
#     fac*=i

# print(f"factorial of given  number is {fac}")


#Q10 from 1  to n  find the print the sum of all  even number  and all odd number separately

# n = int ( input("Enter a number till to find the  sum of odd and even numbr :"))
# odd=0
# even =0
# for i in range (n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i

# print(f"The sum of even number is :{even} \nThe sum of odd number is :{odd}")
 


#Q11 Display all number  that divide the input number  exactly (no remainder)

# n= int(input("Enter a number you want to find this all factor :"))

# print(f"{n} all factor--> ")
# for i in range(1,n+1):
#     if n%i==0:
#         print(f"{i}")

#Q12 add up all the factor  in the  previous  question (excluding or including  the number itself - your choice )
# n= int(input("Enter a number you want to find  the sum of  all factor :"))
# sum =0
# print(f"{n} all factor--> ")
# for i in range(1,n+1):
#     if n%i==0:
#         print(f"{i}")
#         sum+=i


# print(f"Sum of all factor is {sum}")


#Q13 power  calculation (a^b) , input base (a) and exponent (b) , and  calculate  the result  using a loop (without using **).

# print("Find the power ")

# a=int(input("Enter base :"))
# b=int(input("enter exponent :"))
# power=1
# for i in range (b):
#     power*=a

# print(f"{a} base {b} Exponent power is :{power}")    

#Q14 prime number check , accept a number  and check it is is divisible only by 1 and itself (i.e., prime or not )

# n = int(input("Enter a number to check it is prime or not :"))

# tmp=0

# for i in range(2,n):
#     if n!=1:
#         if n % i==0:
#             tmp+=1
#             break
#     else:
#         tmp=2    
# if tmp == 0 :
#     print("its a prime number ")
# elif tmp==2:
#     print("its a unity number ")
# else :
#     print("its not a prime number ")    

# write your code here

# write your code here
# s,e = map(int,input().split())
# r=0
# n=0
# b=0
# c=0
# for i in range(s,e+1,1):
#     a=i
#     b+=1
#     while i>0:
#         n=i%10
#         r=(r*10)+n
#         i//=10
#    # print(r)
#     if(a==r):
#         print(a)
#     else:
#         c+=1
# if c==b:
#     print("Not palindrom number ")


#----------------------------------------------------------WHILE LOOP --------------------------------------------------------------------

#Q1 print each  digit  (Reverse order)
#break a number into individual digit and print them starting from the last digit
# n = int(input("Enter a number you want to print in reversed order :"))
# r=0
# a=0
# while n > 0:
#     r = n % 10
#     print (r,end=" ")
#     n//=10


#Q2 Sum of all digit , add all the digit of a number (e.g., 123 -> 1+2+3=6)

# num =int(input("Enter a number :"))
# sum =0

# while num > 0:
#     r=num%10
#     sum+=r
#     num//=10

# print("\nSum of all digit :",sum)    


#Q3 check number is palindrom or not 

# n = int(input("Enter a number to check its palindrom or not :"))
# r=0
# rev =0
# c=n
# while n>0:
#     r=n%10
#     rev = (rev *10)+r
#     n//=10

# if rev == c:
#     print("this is palindrom number ..")
# else:
#     print("this is not a palindrom number ..")    


#Q4 Automorphic number 
# A number is automorphic number if its square ends with the number itself (e.g 5**2 =25 , 76**2 = 5776)

# num = int(input("Enter a number to check its automorphic and not :"))
# copy =num
# copy1=num 

# copy = copy *copy
# r=0
# rev=0
# while num > 0:
#     r=copy%10
#     rev = (rev * 10) + r
#     num//=10
#     copy//=10

# rev1=0
# while rev > 0:
#     r=rev%10
#     rev1 =(rev1*10 )+r
#     rev //=10    
# print (rev1)
# print(copy1)
# if copy1 == rev1:
#     print("Its Automorphic number ")
# else:
#     print("its not a Automorphic number ")      


#Enter  two string and Check it is anagram or not 

str1=input ("Enter frist strig :")
str2=input("enter second string :") 
count=0
for i in range(len(str1)+1):
    if str1[i] not in str2:
        count+=1

if count==0:
    print("this is anagram ")
else :
    print("this is not anagram ")    