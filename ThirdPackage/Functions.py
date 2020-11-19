#תרגיל 10.1 חוברת
"""def highest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(highest(1,2,3))"""
#תרגיל 10.2 חוברת
"""def tupsum(tup):
    sum = 0
    for i in tup:
        sum+=i
    return sum"""
#תרגיל 10.3 חוברת
"""def mult(tup):
    sum=1
    for i in tup:
        sum*=i
    return sum"""
#תרגיל 10.4 חוברת
"""def strg(strg):
    return strg[::-1]
print(strg('sagi'))"""
#תרגיל 10.5 חוברת
"""def rangenum(low, num, high):
    if low<num<high:
        return True
    else:
        return False
print(rangenum(8,4,3))"""
#תרגיל 10.6 חוברת
"""def cap(string):
    lower = 0
    upper = 0
    for i in string:
        if 65<=ord(i)<=90:
            upper+=1
        elif 97<=ord(i)<=122:
            lower+=1
    return f"the capital letters:{upper} || the lower letters: {lower}"
print(cap("AbAle"))"""
#תרגיל 10.7 חוברת
"""list2 = [1,1,1,4,3,6,5]
def dup(list1):
    return list(set(list1))
print(dup(list2))"""
#תרגיל 10.8 חוברת
"""def isprime(num):
    for i in range(2,10):
        if num%i == 0 and num!=i:
            return False
        else:
            r = True
    return r
print(isprime(7))"""

#10.9 חוברת
"""list1 = [1,4,8,9,11,14]
def evensum(list1):
    sum=0
    for i in list1:
        if i%2 == 0:
            sum+=i
    return sum"""
#10.10 חוברת
"""def strg(strg):
    if strg[::-1] == strg: return True
    else: return False"""

#פונקציות תרגילים 2
#תרגיל 1 דף 2
"""def remA(strg):
    strg = list(strg)
    for i in strg:
        if i == 'A' or i == 'a':
            strg.remove(i)
    new = ''
    for i in range(len(strg)):
        new += strg[i]
    return new
word = input("Enter a word: \n")
print(remA(word))"""
from touse import targil2functions
#תרגיל 2 דף 2
"""strng = input("Enter a word: \n")
action = input("what to do? type reverse to reverse the word and triple to reverse 3 times: \n")
if action == 'reverse':
    strng = targil2functions.revs(strng)
    print(strng)
elif action == 'triple':
    for i in range(3):
        print(targil2functions.revs(strng),end=' ')
else:
    print('error')"""
#תרגיל 3 דף 2
"""def func(word):
    for i in range(len(word)):
        print(word[0]+word[len(word)-1])
text = input("Enter a word to print the first and last letter of for times = length of the word \n")
func(text)"""


#תרגיל 5 דף 2
"""def rounddd(num):
    newnum=num-int(num)
    if newnum > 0.5:
        return int(num)+1
    elif newnum <0.5:
        return  int(num)
    else:
        return num
num1 = float(input("Enter one number: \n"))
num2 = float(input("Enter another number: \n"))
print(roundd(num1)+roundd(num2))"""




