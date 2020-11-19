#https://pynative.com/python-string-exercise/
#תרגיל 1

"""word = input("Enter a word: \n")
length = 0
for c in word:
    length+=1

if length >= 7 and (length%2)!=0 :
    print(word[(length-3)//2:((length-3)//2)+3])
elif length < 7:
    print("Not long enough")"""

#תרגיל 2
"""s1 = "Ault"
s2 = "Kelly"
middle = len(s1)//2
left = s1[:middle]
right = s1[middle:]
print(left+s2+right)"""

#תרגיל 3
"""s1 = "America"
s2 = "Japan"
mid1 = len(s1)//2
mid2 = len(s2)//2
print(s1[0]+s2[0]+s1[mid1]+s2[mid2]+s1[len(s1)-1]+s2[len(s2)-1])"""

#תרגיל 4
"""str1 = "PyNaTive"
leftstr = ''
rightstr = ''
for c in str1:
    if ord(c)>=97 and ord(c) <= 122:
        leftstr+=c
    elif ord(c)>=65 and ord(c) <= 90:
        rightstr+=c
print(leftstr+rightstr)"""
#תרגיל 5
"""str1 = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0
for c in str1:
    if (ord(c)>=97 and ord(c) <= 122) or (ord(c)>=65 and ord(c) <= 90):
        chars+=1
    elif ord(c)>=48 and ord(c) <=57:
        digits+=1
    else:
        symbols+=1
print(f"Total counts of chars, digits,and symbols\n\nChars:{chars}\nDigits:{digits}\nSymbols:{symbols}")"""
#תרגיל 7
"""s1 = "Ynf"
s2 = "PYnative"
flag = True
for c in s1:
    if c in s2:
        continue
    else:
        flag = False
print(flag)"""
#תרגיל 7 עמוד שני
"""while(True):
    str1 = input("enter a string that contains the words not and poor: \n")
    checkword = ''
    poor = False
    not1 = False
    for c in str1:
        for i in range(len(str1)):
                if str1[i] == 'p':
                    if str1[i + 1] == 'o':
                        if str1[i + 2] == 'o':
                            if str1[i + 3] == 'r':
                                poor = True
                                checkword = 'poor'
                elif str1[i] == 'n':
                    if str1[i+1] == 'o':
                        if str1[i+2] == 't':
                            not1 = True
    print("poor? ",poor)
    print("not?",not1)"""
#תרגיל 8
"""str1 = "Welcome to USA. usa awesome, isn't it hail"
count=0

for i in range(len(str1)):
    if str1[i] == 'U':
        if str1[i+1] == 'S':
            if str1[i+2] == 'A':
                count+=1
    elif str1[i] == 'u':
            if str1[i+2] == 'a':
                count+=1
print(count)"""
#תרגיל 9
"""string = "English = 78 Science = 83 Math = 68 History = 65"
numbers = ''
divider = 0
sum=0
for i in range(len(string)):
    if ord(string[i]) >= 48 and ord(string[i]) <= 57:
        numbers+=string[i]
    elif (ord(string[i]) <= 48 or ord(string[i]) >= 57) and numbers != '':
        sum += int(numbers)
        divider+=1
        numbers = ''
if numbers != '':
    sum += int(numbers)
    divider+=1

print(f"the sum is:{sum} and the average is: {sum/divider}")"""
#תרגיל 24 עמוד שני
"""word = input("enter a word: \n")
word2 = input("enter another word to check if its in the first one: \n")
count = 0
for c in word:
    for i in range(len(word2)):
        # print(c+" "+word2[i])
        if c == word2[i]:
            count+=1
    #print("=====================")
if count == len(word2):
    print(True)
    count=0

else:
    print(False)"""
#תרגיל 25 עמוד שני
"""word = input("Enter a text to encrypt: \n")
for c in word:
    print(chr(ord(c)+3),end='')"""

#תרגיל 19 עמוד שני
"""string = input("Enter a string:")
char = input("enter a char to print all the string thats after that char: \n")
for i in range(len(string)):
    if string[i] == char:
        string2 = string[i:]
print(string2)"""