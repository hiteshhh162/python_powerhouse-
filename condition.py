# #Define three number and find which one is greater  
# a=10
# b=20
# c=30

# if a>b and a>c:
#     print("A is greater ")

# elif b>c:
#     print("b is greater")
# else :
#     print("c is greater ")        

#Q2-> take two number from user  inputs and determines which number is greater - or if they are equal 

# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))

# if num1==num2:
#     print("both number are equal ")
# elif num1>num2:
#     print("number one is greater than number two ")
# elif(num1<num2):
#     print("number second is greater than number one ")        


#Q3  accept a gender input ('m') or ('f') and print  a greeeting like "hello sir " or "Hello ma'am ".

# gen=input("Enter gender (male for 'm' or female for 'f')")

# if gen=='m' or gen=='M':
#     print("Hello Sir ")
# elif gen=='f' or gen == 'F':
#     print("Hello Ma'am")
# else :
#     print("Please enter a valid gender ")        


#Q4  accept a number from the user and check whether it's even or odd using module (%)

# num = int(input("Enter a number :"))

# if num%2==0:
#     print("number is even ")
# else :
#     print("Number is odd ")    



#Q5 input name and age  id age >18 print "eligible  to vote"  , if not print how many years are left 

# name =input("Enter name :")
# age =int(input("Enter age :"))

# if age >=18 :
#     print("Eligible to vote ")
# else :
#     print(f"{18-age} years are left to become a eligible ")    



#Q6 take  an integer (1-7)  and print corresponding weekday ( 1= Monday, 2= tuesday...) handle invalid 'input too

# day = int(input("Enter day number (1-7):"))

# if day ==1:
#     print("1=Monday ")
# elif day ==2:
#     print("2==Tuesday ")    
# elif day==3:
#     print("3==Wednesday" )
# elif day ==4:
#     print("4==Thursday ")
# elif day ==5:
#     print("5==Friday ")
# elif day ==6:
#     print("6==Saturday ")
# elif day ==7:
#     print("7==Sunday ")
# else :
#     print("Please enter a valid number ")


#Q7 accept three number and find the  greatest number  and also find if 2 are equal and find if  all are equal

# a=int(input("Enter first number :"))
# b=int(input("Enter second numbre :"))
# c=int(input("Enter third number :"))


# if a==b and a==c:
#     print("All number are equal ") 
# elif a==b or b==c or c==a: 
#     print("Two number are equal ")
# elif a>b and a>c :
#     print("A is largest number ")
# elif b>c:
#     print("B is largest number ") 
# else :
#     print("C is largest number ")       
       


#Q8 input a year and check it is leap year or not   using proper rules divisible by 4 not by 100 unless divisivle by 400

# year = int (input("Enter a year "))

# if year %4==0:
#     if year % 100==0 and year %400!=0:
#          print("This year is not a leap year ")
#     else:
         
#         print("This year is leap year ")
# else :
#      print("This year is not a leap year ")    


#Q9 ask for purchase amount . Apply discount based on thresholds : e.g; above 1000 -> 10% off 
#, above 5000->20% off  print final bill , (you can also design  a shop - like interface later )

# pur_ammount= float(input("Enter a purchse amount :"))

# if pur_ammount>=5000:
#     dis=pur_ammount*20/100
#     print(dis)
#     print("You got a 20% discount , Your final pay bill is :",pur_ammount-dis)

# elif pur_ammount>=1000:
#     dis=pur_ammount*10/100
#     print("You got a 10% discount ,Your final pay bill is :",pur_ammount-dis)    

# else:
#     print("Your final pay bill is :",pur_ammount) 



#Q10 Accept a sigle character and check its  vowel (a,e,i,o,u) or not and also handle invalid character 


# ch=input("Enter a single character :")
# if ch=='a' or ch=='e' or ch=='i' or ch=='u' or ch=='o' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
#     print("its a vowel ") 
# elif (ch>='A' and ch<='Z' or ch>='a' and ch<='z')and ch!='a' or ch!='e' or ch!='i' or ch!='u' or ch!='o' or ch!='A' or ch!='E' or ch!='I' or ch!='O' or ch!='U':
#     print("its a consonant  ")
# else:
#     print("Please enter a valid choice ")        

#Second methods 
# if ch in "aeiouAEIOU":
#     print("Your character is vowel ")
# else :
#     print("your character is consonant ")    



#Q11 reverse number 

# num1 = int(input("Enter a number :"))
# n=int(0)
# r=int(0)

# while(num1 > 0):
#     n=num1%10
#     r=(r*10)+n
#     num1//=10
# print("reverse number :",r)    
str = input()

length =int(len(str))
if length % 2==0:
    length=int(length-1)
length/=2

print(str[int(length)])
