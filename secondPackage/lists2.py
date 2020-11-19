#תרגיל 5.6
"""list = [1,2,3,4,5,6,7,8,9,10]
list2 = list[-3:]
listodd = []
print(list2[::-1])
for i in range(len(list)):
    if list[i] % 2 == 0:
        listodd+= [list[i]]
print(listodd)
list3 = list[0::2]
print(list3)
for i in range(3): #סעיף 5
    num = int(input("enter a number: "))
    if i < 2:
        list[4+i]=num
    else:
        list+=[num]
print(list)
for i in range(len(list)):
    list[i]*=3
print(list)
list4 = [list[-1]] +[list[0]]
print(list4)"""

#excersize 2 pynative
"""list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
for i in range(len(list1)):
    list1[i]+=list2[i]
print(list1)"""

#excersize 5 pynative
"""list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(4):
    print(list1[i],list2[3-i])"""

#excersize 6 pynative
"""list1 = ["Mike", "", "Emma", "Kelly", "", "Brad","itzik","","","avi"]
list2 = []
for i in range(len(list1)):
    if list1[i]!="":
        list2 += [list1[i]]
        continue
print(list2)"""
#excersize 7 pynative
"""list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
i=2
list1[i][i]+=[7000]
print(list1)"""
#Exercise Question 8
"""list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub = ["h", "i", "j"]
list1[2][1][2]+=sub
print(list1)"""
#Exercise Question 9
"""list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
print(list1)"""
#Exercise Question 10
"""list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = []
for i in range(len(list1)):
    if list1[i] == 20:
        continue
    elif list1[i] !=20:
        list2 += [list1[i]]
print(list2)"""

set = {20,33,44,55,66}
for i in set:
    print(i)