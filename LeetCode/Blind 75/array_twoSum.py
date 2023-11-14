def twoSum(nums, target):
    num_set = set()

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_set:
            return [nums.index(complement), i]
        num_set.add(num)

print(twoSum([2,7,11,15],9))