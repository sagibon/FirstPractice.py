#דף 3
#len תרגיל 1
"""listone = [1,2,3,4,5,6,7,8]
def leng(list1):
    count = 0
    for i in list1:
        count+=1
    return count"""
#count תרגיל 2
"""listone = [1,2,2,4,5,6,2,8]
num = 2
def cont(list1,num):
    count = 0
    for i in list1:
        if i == num:
            count+=1
    return count
print(cont(listone,num))"""
#תרגיל find 3
"""listone = [1,2,2,4,5,6,2,8]
num1 = 2
start1 = 0
def fynd(list1,num,start = 0):
    'works good' #הערה על הפונקציות שרואים בHELP
    for i in range(start,len(list1)):
        if list1[i] == num:
            return i

print(fynd(listone,num1,0))
help(fynd)"""
#תרגיל max 4
"""listone = [1,2,2,11,5,6,2,8]
def maxx(list1):
    check = 0
    for i in range(len(list1)):
        if list1[i]>check:
            check = list1[i]
    return check
print(maxx(listone))"""
#tolist תרגיל 5
"""d= {'name':1,'it':2,'a':3,'adi':4}
def tolist(data):
    if type(data) == int or type(data) == float or type(data) == bool:
        print('Error')
        return None
    newlist = []
    for i in data:
        newlist+=[i]
    return newlist
print(tolist(11))"""
#remove תרגיל 6
"""def remv(list1,delet):
    newlist = []
    for i in list1:
        if i == delet:
            continue
        elif i != delet:
            newlist+=[i]
    return newlist
list1 = [1,2,3,4]
print(id(list1))
print(id(remv(list1,1)))"""
#dictionary keys תרגיל 7
"""d= {'name':1,'it':2,'a':3,'adi':4}
def kis(d1):
    newlist = []
    for i in d1: newlist+=[i]
    return newlist
print(kis(d))"""
#תרגיל dictionary values 8
"""d= {'name':1,'it':2,'a':3,'adi':4}
def kis(d1):
    newlist = []
    for i in d1: newlist+=[d1[i]]
    return newlist
print(kis(d))"""
# dictionary items תרגיל 9
"""d= {'name':1,'it':2,'a':3,'adi':4}
def itmes(d):
    tuplist = []
    for i in d:
        tup = (i,d[i])
        tuplist+=[tup]
    return  tuplist
print(itmes(d))"""
#תרגיל 10
