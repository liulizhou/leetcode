class Solution:
    def __init__(self):
        pass

    def trap(self, nums):
        max_idx = 0
        max_value = 0
        if len(nums) < 3:
            return 0
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_idx = i
                max_value = nums[i]
        a = b = 0
        water = 0
        for b in range(0, max_idx + 1):
            if nums[b] < nums[a]:
                water = water + nums[a] - nums[b]
            else:
                a = b
        a = b = len(nums) - 1
        for b in range(len(nums) - 1, max_idx - 1, -1):
            if nums[b] < nums[a]:
                water = water + nums[a] - nums[b]
            else:
                a = b
        return water

if __name__ == '__main__':
    # nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    nums = [2, 0, 2]
    s = Solution()
    print(s.trap(nums))