import random
#excerisze 1
"""
curryear = 2020
name = input("enter ur name:")
age = int(input("enter ur age:"))
print("sagi will be 100 years old in ",(curryear - age +100))
#2
#same as 1, no point
#3
num = int(input("enter a number to determine odd or even:"))
if num%2 == 0:
    print("Even")
elif num%2 != 0:
    print("Odd")
"""
#7
attempts = 0
print("think about a number, the program will guess one")
compnum = random.randrange(1,100)
while(True):
    attempts+=1
    text = input("Is %d the number? higher or lower" %compnum)
    if "yes" in text:
        print(f"{compnum} is the correct number, took {attempts} attempts")
        break
    elif "higher" in text:
        compnum = random.randrange(compnum, 100)
    elif "lower" in text:
        compnum = random.randrange(1,compnum)
    else:
        print("Succ my dicc")




#8
string = input("Insert a long string to reverse its text: ")
for i in string[::-1]:
    print(i)
#9
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
for i in range(num1,num2+1,1):
    if i%2==0:
        print(i, end=" ")







