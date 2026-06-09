# def kidsWithCandies(candies, extracandies):
#     maxcandies = max(candies)
#     result = []
#     for candy in candies:
#         if candy+extracandies >= maxcandies:
#             result.append(True)
#         else:
#             result.append(False)

#     return result

def kidsWithCandies(candies, extracandies):
    return [(candy+extracandies>=max(candies)) for candy in candies]

print(kidsWithCandies([2, 3, 5, 1, 3], 3))