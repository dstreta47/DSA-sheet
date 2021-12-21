#TC = O(n)
def reverse_array(l1):
    l = 0
    r = len(l1)-1

    while(l<r):
        l1[l],l1[r] = l1[r],l1[l]
        l+=1
        r-=1
    return l1       
#TC = O(n)
def reverse_array_recursive(l1,start,end):
    if start>=end:
        return

    l1[start],l1[end] = l1[end],l1[start] 
    reverse_array_recursive(l1,start+1,end-1)
    
#TC = O(n)
def reverse_by_slic(l1):
    return l1[::-1]   

l1 = [1,2,3,4,5,6]
print(reverse_by_slic(l1))
print(l1)

