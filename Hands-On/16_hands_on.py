# nums = []

# for i in range(5,100,5):
#     nums.append(i)

# print(nums)

# l = print([i for i in range(5,100,5)])
# print(l)


# This is extra question's solution
num = int(input("Enter a number: "))

def even(num):
    nums = []
    for i in range(0,num+1,2):
        nums.append(i)
    return nums

print(even(num))