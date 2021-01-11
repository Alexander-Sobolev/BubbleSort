# Bubble sort

nums = [2,8,5,1,3,9,7]
print(nums)

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)
