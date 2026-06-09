
# def fizzBuzz(n):
#     result = []
#     for x in range(1, n+1):
#         word = ''
#         if x % 3 == 0:
#             word += 'Fizz'
#         if x % 5 == 0:
#             word += 'Buzz'
#         result.append(word or x)
#     return result

#Less Modulo Operations
def fizzBuzz(n):
    result = []
    for i in range(1, n+1):
        if(i % 15 == 0):
            result.append('FizzBuzz')
        elif(i % 3 == 0):
            result.append('Fizz')
        elif(i % 5 == 0):
            result.append('Buzz')
        else:
            result.append(i)
    return result
        

print(fizzBuzz(15))
