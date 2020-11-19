#excersize 1
num1 = 123
num2 = 456
print(f"multiply:{num1*num2} \naddition:{num1+num2} \nsubstraction:{num1-num2} \ndivision:{num1/num2}")
#excercise 2
day = '03'
month = '11'
year = '20'
print(day+'/'+month+'/'+year)
#excersize 3
num = int(input("enter a 3 digit number:"))
print(f"{num%10}{num%100//10}{num//100}")
#excersize 4
name = input("Enter ur name:")
age = input("enter ur age:")
currentyear = input("enter current year:")
futureyear = input("enter future year to calculate ur age then:")
futureyear = int(futureyear)
currentyear = int(currentyear)
age = int(age)
if futureyear < currentyear:
    print("אני אזיין אותך")
currentyear = futureyear-currentyear
print(f"{name} will be {currentyear+age} in {futureyear}")
#excersize 5
a = input("Enter first digit:")
b = input("Enter second digit:")
c = input("Enter third digit:")
print(a+b+c)
print(2*(int(a+b+c)))

