#index scans the list from the beginning, use dict instead
# Time complexity:
# Sorting: O(n log n)
# index() inside a loop: O(n) × n
# Total: O(n²)
# def smallerThanCurrent(nums): 
#     sortednums = sorted(nums) 
#     result = [] 
#     for i in nums: 
#         result.append(sortednums.index(i)) 
#     return result 

# Time complexity:
# Sorting: O(n log n)
# Building dictionary: O(n)
# Lookup for each element: O(n)
# Total: O(n log n)
def smallerThanCurrent(nums):
    rank = {}
    sortednums = sorted(nums) #[1, 2, 2, 3, 8]
    for i, num in enumerate(sortednums):
        print(i, num)
        if num not in rank:
            rank[num] = i
    print(rank)
    return [rank[num] for num in nums]

nums = [8, 1, 2, 2, 3]
print(smallerThanCurrent(nums))


