"""def itzik(list1, size):
    for i in list1[:size]:
        print(i,end=',')
word = input("enter a string: \n")
leng = int(input("How much of the string it should print: \n"))
print(itzik(word,leng))"""
list1 = [1,2,3,4,5,6,7,8]
x = list1.pop(1)
print(list1)
print(x)
print(list1.index(3,5))