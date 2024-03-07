lst=[20,11,15,4,18,6,2,13,8]
print(lst)
for i in range(len(lst)):
    small=i
    j=0
    for j in range(i+1,len(lst)):
        if lst[small]>lst[j]:
            small=j
    lst[small],lst[i]=lst[i],lst[small]
    print(lst)   
