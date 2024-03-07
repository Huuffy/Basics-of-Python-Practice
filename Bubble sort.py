lst=[12,4,11,13,1,2,3,8,7,9]
for i in range(len(lst)):
    j=0
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            print(lst)
print('Final ans \n',lst)
