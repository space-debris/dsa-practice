def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # a.sort()
    # return a[-2],a[1]

    largest=smallest=a[0]
    seclargest=-1
    secsmallest=a[n-1]
    for i in range(1,n):
        if a[i]>largest:
            seclargest=largest
            largest=a[i]
        elif a[i]>seclargest and a[i]<largest:
            seclargest=a[i]
        if a[i]<smallest:
            secsmallest=smallest
            smallest=a[i]
        elif a[i]>smallest and a[i]<secsmallest:
            secsmallest=a[i]
    return seclargest, secsmallest

            