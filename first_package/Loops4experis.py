"""lowest = 100000
while(True):
    inpt = int(input("enter a number: "))
    if inpt > 0 and inpt<lowest:
        lowest = inpt

    if inpt == 0:
        break
print(f"the lowest real integer is {lowest}")"""
#targil 2 lolaot 4
"""num = int(input("enter a number to show his left digit"))
while num >= 10:
    num//=10
print(num)"""
#תרגיל 3 לולאות 4
"""highest=0
count = 0
while count!=7:
    num = int(input("Enter a number: "))
    if num > highest:
        highest = num
        highestcount = count
    count+=1
print(f"Highest is {highest} in location {highestcount}")"""
#תרגיל 4 לולאות 4
"""digits = 1
num = int(input("enter a number to reverse"))
numcheck = num
regularnum = num
#check digits
while numcheck >= 10:
        numcheck//=10
        digits+=1
count = digits
numcheck = 0
while digits>0:
    num = regularnum
    num = (num // (10 ** (digits-1)) % 10)
    numcheck+=(num*10**(count-digits))
    digits-=1
print(f"the reversed number is {numcheck} and the double is {numcheck*2}")"""



