def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    largest=0
    seclargest=1
    if a[largest]>a[seclargest]:
        pass
    elif a[seclargest]>a[largest]:
        largest,seclargest=seclargest,largest
    for i in range(2,n):
        if a[i]>a[largest]:
            largest=i
        elif a[i]>a[seclargest] and a[i]<a[largest]:
            seclargest=i
    
