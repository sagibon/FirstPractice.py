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
"""str1 = input(" :תרשום מילה")
str2 = input(" :תרשום עוד מילה")
status = True
for c in str1:
    if c in str2:
        continue
    else:
        status = False
print(status)
#תרגיל 8
str1 = "Welcome to USA. usa awesome, isn't it?"
count=0
word1 = ''
word2 = ''
for c in str1:
    if c == 'U' or c == 'S' or c == 'A':
        word1+=c
    if c == 'u' or c == 's' or c == 'a':
        word2+=c
if word1 == 'USA':
    count+=1
if word2 == 'usa':
    count+=1
print(count)"""

#תרגיל 7 עמוד שני
while(True):
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
    print("not?",not1)