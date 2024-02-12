# brute force approach
def removeDuplicates(arr,n):
    unique=set()
    unique_elm=0
    for i in range(n):
       if arr[i] not in unique:
            unique.add(arr[i])
            unique_elm+=1

        
    return unique_elm