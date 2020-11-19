dir1 = {1:'K',2:'88888888',3: '12',4:'10', 5:'610' , 6:'138644020' ,7: '315250589', 8:'shemhalakochs'}
#need to add 3 chars in 8

strg = 'k12345678120000001061000001386400200315250589tbridgeconsultin00000000420990000000000000012305620102011000504000000000000000000'
print(len(strg))
list1 = list(strg)
for i in list1:
    if i == '}':
        list1.remove(i)
    elif i == '{':
        list1.remove(i)
    else:
        continue
print(list1)