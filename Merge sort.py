def mergesort(lst,l,r):#l=left   r=right
    if l<r:
        mid=(l+(r-1))//2
        mergesort(lst,l,mid)
        mergesort(lst,mid+1,r)
        merge(lst,l,mid,r)
        print(lst)
        
def merge(lst,l,mid,r):
    n1=mid-l+1
    n2=r-mid
    llst=[0]*(n1)
    rlst=[0]*(n2)
    for i in range(0,n1):
        llst[i]=lst[l+i]
    for i in range(0,n2):
        rlst[i]=lst[mid+1+i]
    i=0#llst
    j=0#rlst
    k=l
    while i<n1 and j<n2:
        if llst[i]<=rlst[j]:
            lst[k]=llst[i]
            i+=1
        else:
            lst[k]=rlst[j]
            j+=1
        k+=1
    while i<n1 :
        lst[k]=llst[i]
        i+=1
        k+=1
    while j<n2:
        lst[k]=rlst[j]
        j+=1
        k+=1

lst=[5,18,6,2,1,0,17,19]
mergesort(lst,0,(len(lst)-1))
