class Solution:
    def bns(self, nums):
        size = len(nums)
        left , right = 0, size - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

    def lns(self, nums):
        i = 0
        while nums[i] < nums[i + 1]:
            i = i + 1
        return i
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 7, 5, 4, 3, 2, 1]
    flags = 1
    s = Solution()
    if flags == 1:
        print(s.lns(nums))
    elif flags == 2:
        print(s.bns(nums))