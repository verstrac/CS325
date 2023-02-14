# Caleb Verstraete
# CS325
# 02/03/2023

def main():
    nums = [7,0,0,0,6]
    print(max_independent_set(nums))

def max_independent_set(nums):
    max_sum = [0 for x in range(len(nums) + 1)]
    max_set = [[] for x in range(len(nums) + 1)]
    if len(nums) == 0:
        return max_set
    if len(nums) == 1 and nums[0] >= 0:
        return nums
    elif len(nums) == 1 and nums[0] < 0:
        return max_set
    elif nums[0] < 0:
        max_set[1] = []
        max_sum[1] = 0
    else:
        max_set[1] = [nums[0]]
        max_sum[1] = nums[0]

    for index in range(2, len(max_set)):
        max_sum[index] = max(max_sum[index - 2] + nums[index - 1], max_sum[index - 1])
        left_side = max_sum[index - 2] + nums[index - 1]
        right_side = max_sum[index - 1]
        if left_side >= right_side:
            max_set[index] = max_set[index - 2].copy()
            max_set[index].append(nums[index - 1])
        else:
            max_set[index] = max_set[index - 1].copy()


    return max_set[len(max_set) - 1]

def max_set_helper(nums, index):
    if index < 0:
        return 0
    if nums[index] < 0:
        return max_set_helper(nums, index - 1)
    else:
        return max(max_set_helper(nums, index - 2) + nums[index], max_set_helper(nums, index - 1))


if __name__ == '__main__':
    main()