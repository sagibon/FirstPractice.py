#orly's site url https://pynative.com/python-list-exercise-with-solutions/
#question1
aLsit = [100, 200, 300, 400, 500,600]
print(aLsit[1::2])
#question2
"""list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list4 = []
for i in range(len(list2)):
    list3 = [list1[i]+list2[i]]
    list4+=list3
print(list4)"""
#question3
'''alist = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(alist)):
    alist[i]=alist[i]**2
print(alist)'''
aList = [1, 2, 3, 4, 5, 6, 7]
if 1 in aList:
    print(True)
else:
    print(False)
aList = [x * x for x in aList]
print(aList)
#question4
"""list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
resList = [x+y for x in list1 for y in list2]
print(resList)"""
"""list1 =["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list1[:1]+list1[1:])"""

