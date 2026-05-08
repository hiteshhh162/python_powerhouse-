import random 
num = random.randint(1,100)
tries = 0
guessed = int (input("guess the number  between 1 to 100"))

if guessed == num:
    print("Congratulation  you found your number ")
