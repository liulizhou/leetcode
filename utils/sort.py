import random
# sort
class Solution:
    def heap_sort_pos(self, nums):
        def max_heap(nums, root, size):
            p = root
            while(p * 2 + 1 < size):
                l, r = p * 2 + 1, p * 2 + 2
                if r < size and nums[l] < nums[r]:
                    nex = r
                else:
                    nex = l
                if nums[nex] > nums[p]:
                    nums[nex], nums[p] = nums[p], nums[nex]
                    p = nex
                else:
                    break

        size = len(nums)
        for i in range(size - 1, -1, -1):
            max_heap(nums, i, size)
        for i in range(size - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            max_heap(nums, 0, i)

    def heap_sort_rev(self, nums):
        def min_heap(nums, root, size):
            p = root
            while(2 * p + 1 < size):
                l, r = 2 * p + 1, 2 * p + 2
                if r < size and nums[l] > nums[r]:
                    nex = r
                else:
                    nex = l
                if nums[nex] < nums[p]:
                    nums[nex], nums[p] = nums[p], nums[nex]
                    p = nex
                else:
                    break
        size = len(nums)
        for i in range(size - 1, -1, -1):
            min_heap(nums, i, size)
        for i in range(size - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            min_heap(nums, 0, i)

    def quick_sort(self, nums):
        def part(nums, l, r):
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            i = l - 1
            for j in range(l, r):
                if nums[j] < nums[r]:
                    i = i + 1
                    nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def sort(nums, l, r):
            if l >= r:
                return
            mid = part(nums, l, r)
            sort(nums, l, mid - 1)
            sort(nums, mid + 1, r)
        l, r = 0, len(nums) - 1
        sort(nums, l, r)


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 7, 9]
    s = Solution()
    # s.heap_sort_pos(nums)
    # s.heap_sort_rev(nums)
    s.quick_sort(nums)
    print(nums)