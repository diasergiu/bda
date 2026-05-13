# 1

def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
# O(log n) time complexity O(1) space complexity halves the search space with each iteration

# nums = [2, 5, 8, 12, 16, 23, 38, 56, 72]
# print(binary_search(nums, 23))

# 2

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)
# O(nlog n) time complexity O(n) space complexity splits the list into halve log n times and merges n elements each time

# print(merge_sort([7, 2, 9, 1, 5, 3]))
# print(merge_sort(["banana", "apple", "cherry", "date"]))

# 3 

def count_pairs(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                count += 1
    return count


# print(count_pairs([10, 20, 30, 40]))

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# print(fib(6))


def permute_count(data):
    if len(data) <= 1:
        return 1

    total = 0
    for i in range(len(data)):
        rest = data[:i] + data[i + 1:]
        total += permute_count(rest)
    return total


# print(permute_count([1, 2, 3, 4]))

# 3

def binary_searchCount(data, target):
    left = 0
    right = len(data) - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        count += 1

    return count

# print(binary_searchCount([2, 5, 8, 12, 16, 23, 38, 56, 72], 23))

# 4

def count_pairsModified(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data), 1):
            if data[i] == data[j]:
                count += 1
    return count

print(count_pairsModified([10, 20, 30, 40, 20, 30, 40]))