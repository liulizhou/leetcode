def BinarySearch(numbers, target):
    left = 0
    right = len(numbers) - 1
    while(left < right):
        mid = (left + right) // 2
        if numbers[mid] < target:
            left = mid + 1
        elif numbers[mid] > target:
            right = mid
        else:
            return mid
    return left

if __name__ == "__main__":
    # numbers = [1, 3, 4, 7, 8, 10, 12, 13, 15, 16, 17, 19, 20]
    numbers = [12]
    target = 12
    print(BinarySearch(numbers, target))