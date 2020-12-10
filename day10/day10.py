import collections as co

file = open('input.txt', 'r').read().splitlines()

nums = list(map(int, file))
nums.sort()

num_diffs = [b - a for a, b in zip(nums, nums[1:])]

num_diffs.insert(0, 1)
num_diffs.append(3)
c = co.Counter(num_diffs)
print(c[1] * c[3])


counts = [0] * len(nums)

for i, n in enumerate(nums):
    if n > 3:
        break
    counts[i] += 1

for i, n in enumerate(nums):
    for j in range(i-1, -1, -1):
        if n - nums[j] > 3:
            break
        counts[i] += counts[j]

print(counts[-1])
