def productSumDifference(num):
    prod = 1
    sum = 0
    numcopy = num
    while numcopy > 0:
        rem = numcopy % 10
        prod *= rem 
        sum += rem
        numcopy //=10

    return(prod-sum)

print(productSumDifference(4421))