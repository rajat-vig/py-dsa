# def tribonacci(n):
#     if n < 0 or n > 37:
#         return
#     if n == 0:
#         return n 
#     elif n == 1 or n == 2:
#         return 1
#     return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    a, b, c = 0, 1, 1

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c

print(tribonacci(8))


