def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    largest=0
    if n==0:
        return -1
    if n==1:
        return arr[1]
    for i in range(n):
        if arr[i]>arr[largest]:
            largest=i
    return arr[largest]