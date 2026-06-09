def countDivisibleDigits(num):
    numcopy = num
    count = 0
    while numcopy>0:
        rem = numcopy % 10
        if num%rem == 0:
            count+=1
        numcopy = numcopy // 10
    return count


print(countDivisibleDigits(7))