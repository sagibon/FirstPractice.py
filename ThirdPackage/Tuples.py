from random import randrange
#6.1 חוברת
"""tup1 = (1,3,5)
a,b,c = tup1"""
#6.2
"""tup1 = ('i','t','z','i','k')
string = ''
for i in range(len(tup1)):
    string+=tup1[i]
print(string)"""
#6.2 another way
"""tup1 = ('i','t','z','i','k')
    for i in tup1:
        print(i,end='')"""
#6.3 חוברת
"""tup1 = ('sagi','0544665070',20,0,-1)
tup2 = ('name: ','phone: ','age: ','kids: ' ,'kids age: ')
for i in range(len(tup1)):
    print(f"{tup2[i]} {tup1[i]}",end=" | ")"""
#6.4 חוברת
"""list1 = [randrange(1,100) for i in range(10)]
print(list1)
tup1 = tuple(list1)
integer = int(input("Enter a number to add to the tuple: \n"))
tup1+=(integer,)
print(tup1)
newtup = tup1[:4]+tup1[-4:]
print(newtup)
list1 = list(newtup)
list1.pop(0)
print(tuple(list1))"""
#----Tuple excersizes orly-------
#1 targil
"""tup = (1,4,88,10,2,1)
num = int(input("Enter a number to search: \n"))
count = 0
for i in tup:
    if i == num:
        count+=1
print(count)"""
#targil 2
"""tup = (1,2,3)
a,b,c = tup
print(a,b)"""
