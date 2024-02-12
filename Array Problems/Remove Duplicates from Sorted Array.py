# brute force approach
def removeDuplicates(arr,n):
    unique=set()
    unique_elm=0
    for i in range(n):
       if arr[i] not in unique:
            unique.add(arr[i])
            unique_elm+=1
    return unique_elm

def removeDuplicates(arr,n):
    unique=set()
    for i in range(n):
       if arr[i] not in unique:
            unique.add(arr[i])
    unique_list = list(unique)
    for i in range(len(unique_list)):
        arr[i] = unique_list[i]

    return i