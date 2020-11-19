#7.1 חוברת
"""dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}
dic2.update(dic3)
dic1.update(dic2)
print(dic1)
#7.2 חוברת
key = 4
for i in dic1:
    if i == key:
        print(True)"""
#7.3 חוברת
"""dic = dic1.copy() #מעתיק את מה שיש בדיק1 למקום חדש בזיכרון בשם משתנה של מילון אחר
dict = {} #המילון החדש שיכיל את המפתחות והערכים הפוכים
listkeys = []
listvalues = []
for i in dic:
    listkeys+=[i]
    listvalues+=[dic[i]]
print(listkeys, listvalues)""" #לא עבד!! אולי אחזור לזה בהמשך

#עוד דרך לפתור את 7.3
"""dic = {v: k for k,v in dic1.items()} #לולאה שמחליפה את הסדר של כל טאפל שחוזר מהפונקציה ITEMS
print(dic)
print(type(dic))"""
#7.4 חוברת
"""num = int(input("enter a number: \n"))
dict1 = {}
for i in range(1,num+1):
    dict1[i] = i*i
print(dict1)
print(type(dict1))"""
#7.4 חובר5
"""leng = int(input("enter the number of keys: \n"))
dic = {}
for i in range(1,leng+1):
    dic[i] = i*i
print(dic)"""
#7.5 חוברת
"""d1 = {'a':1,'b':2,'c':4}
sum = 0
for i in d1:
    sum+=d1[i]
print(sum)"""
#7.6 חוברת
"""key = int(input("key to delete: \n"))
d1 = {'a':1,'b':2,'c':4}
d1 = {v: k for k,v in d1.items()}
del d1[key]
print(d1)"""
#חוברת 7.7
d1 = {'a':1,'b':2,'c':4, 'd':4}
def itzik():
    print('hi')

itzik()

