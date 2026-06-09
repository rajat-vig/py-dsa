def twoSums(nums, target):
    dmap ={}
    for index, num in enumerate(nums):
        comp = target - num
        print('comp: ', comp)
        if comp in dmap:
            return(dmap[comp], index)
        dmap[num] = index
        
print(twoSums([-1, 0, 2, 1, 5], 7))