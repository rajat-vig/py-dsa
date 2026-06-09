def isPalindrome(num):
    temp = num
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp//10
    return rev == num    



print(isPalindrome(121))