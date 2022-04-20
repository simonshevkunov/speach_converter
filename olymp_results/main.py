n = int(input())

nums = []
res = []

for i in range(n):
    x = input().split()
    nums.append(int(x[0]))
    res.append(int(x[1]))


for i in range(1, n):
    j = i
    while res[j-1] < res[j]:
        if res[j] > res[j-1]:
            res[j], res[j-1] = res[j-1], res[j]
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j -= 1

        if res[j-1] == res[j]:
            if nums[j-1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

        if j == 0:
            break

for i in range(n):
    print(nums[i], res[i])
