from random import randrange

#תרגיל 1 מחרוזות
"""string = input("enter a string, the program will print them without a \n")
for i in string:
    if i == 'a' or i == 'A':
        pass #אם יש a אל תעשה כלום
    else:
        print(i,end='') #אם אין A הדפס את התו בתוך המחרוזת במקום הi"""

#, תרגיל 2גרסה שונה מחזירה סיסמא מוצפנת ויכולה להחזיר יוזר ניימ מההצפנה
"""user = input("Enter a user name: \n")
print("Your new random password is: ")
for i in user:
    print(chr(ord(i)+2), end='')
#return ur user name from password
password = input("\nEnter your password: \n")
for i in password:
    print(chr(ord(i)-2),end='')"""
#תרגיל 2 רגיל
"""user = input("Enter a user name: \n")
print("Your new random password is: ")
for i in range(6):
    print(user[randrange(0,len(user))],end='')"""
#תרגיל 3
word1 = input("Enter a word: \n")
word2 = input("Enter another word: \n")
count = 0
for i in word1:
    for c in word2:
        if i == c:
            count+=1
print(count)
# תרגיל חוברת 2.3
"""address= input("enter a full address with city, street and house number: \n")
address = address.replace(" ","\n")
print(address)"""