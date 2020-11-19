sum=0
num = int(input("enter a number: \n"))
while num%10!=0:
    sum+=num%10
    num=num//10
print(sum)
