lst=[12,1,6,4,9,8,5,13,19,17]
for i in range(0,len(lst)):
    e=lst[i]
    j=i-1
    while j>=0 and e<lst[j]:
        lst[j],lst[j+1]=lst[j+1],lst[j]
        j-=1
        print(lst)
