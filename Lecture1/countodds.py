# def countOdds(low, high):
#     count = 0
#     for i in range(low, high+1):
#         if i % 2 != 0:
#             count+=1
#     return count

# def countOdds(low, high):
#     length = high - low + 1
#     bothodds = low%2 and high%2
#     return (length//2 + bothodds)

#formula to calc oddnumbers from 1 to n => n+1/2
#high+1//2 gives 1 to high odd numbers and low//2 gives odd numbers less than low
def countOdds(low, high):
    return (high+1)//2 - (low//2)



print(countOdds(1, 8))