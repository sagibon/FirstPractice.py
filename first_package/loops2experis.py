#תרגיל 1
highest = 0
counting = 0
sum = 0
grade = int(input("Enter a grade: \n"))
while 0 <= grade <= 100:
    sum+=grade
    counting+=1
    if grade > highest:
        highest = grade
    grade = int(input("Enter a grade: \n"))
print(f"highest {highest} sum {sum} average {(sum/counting)} ")



#תרגיל 2
password = input("Enter a password: \n")
confirm = input("Enter a password to confirm: \n")
if password == confirm:
    print("nice")
else:
    for i in range(5):
        if i == 4:
            print("too many tries")
        confirm = input("Enter a password: \n")
        if password == confirm:
            print("nice")
            break

#תרגיל 3
"""sum=0
num = input("enter a number: \n")
for i in num:
    sum+=int(i)
print(sum)"""