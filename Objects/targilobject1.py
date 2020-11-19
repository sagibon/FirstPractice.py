from Objects.Amud1 import Person as P

person1 = P() #defining person1 as an object instance of the class Person with the name P instead of Person
person1.name = input("Enter a name: \n")
person1.age = int(input("Enter an age: \n"))
person1.kids = int(input("Enter a number of kids: \n"))

person1.show()
if person1.has_children() == True:
    print("Has Children")
else:
    print("Dosent have children")

print(person1.age_group())