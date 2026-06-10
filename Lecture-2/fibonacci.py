# Time Complexity O(n^2) -- For each operation 2 operations are adding
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
        # a, b = b, a + b
    return a


print(fibonacci(9))