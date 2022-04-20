n = int(input())
mas = input().split()
nums = []
for i in mas:
    nums.append(int(i))

for i in range(1, n):
    j = i
    while nums[j-1] > nums[j]:
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            print(' '.join([str(x) for x in nums]))
        j -= 1

        if j == 0:
            break
