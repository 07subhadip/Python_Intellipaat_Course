nums = []

for i in range(1,51):
    nums.append(i * 2)

print(nums)

print(len(nums))
nums.reverse()
print(nums)

index_44 = nums.index(44)
index_44 = 100

print(nums[44])

squared = []

for num in nums:
    squared.append(num ** 2)

print(squared)