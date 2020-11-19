num1 = 0
num2 = 1
num3 = 1
iterations = int(input("How much numbers in fibonacci sequence to display: \n"))
if iterations>=0:
    print(0)
    for i in range(iterations):
        print(num3)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
else:
    print("There are no negative sequesces u piece of crap")

