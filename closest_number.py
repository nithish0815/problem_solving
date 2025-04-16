target=int(input("enter the value:"))
nums = [3,5,7,9,14,20,25,27]

closest = nums[0]
min_diff = abs(target - closest)

for num in nums:
    diff = abs(target - num)
    if diff < min_diff:
        min_diff = diff
        closest = num
print("closest number is:",closest)

