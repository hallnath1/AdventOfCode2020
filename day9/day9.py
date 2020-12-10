file = open('input.txt', 'r').read().splitlines()
nums = list(map(int, file))

# Part A
for i in range(25, len(nums)):
    valid = False
    for j in range(0, i):
        if nums[i] - nums[j] in nums[i-25:i]:
            valid = True
    if valid == False:
        print(nums[i], i)

# Part B
nums = nums[0:523]
crack = 32321523

left = 0
right = 0
total = 0
while total != crack:
    right += 1
    total = sum(nums[left:right])
    if total > crack:
        left += 1
        right -= 1
        total = sum(nums[left:right])

print(min(nums[left:right]) + max(nums[left:right]))
