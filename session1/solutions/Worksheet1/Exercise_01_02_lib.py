def my_len(data):
    count = 0
    for item in data:
        count += 1
    return count

def my_sum(data):
    total = 0
    for item in data:
        total += item
    return total

def my_find(data, target):
    for item in range(len(data)):
        if data[item] == target:
            return item
        

def inBetween(data, low, high):
    find = 0
    for item in data:
        if low <= item <= high:
            find += 1
    return find

def sumEvenNumbers(data):
    total = 0
    for item in data:
        if item % 2 == 0:
            total += item
    return total

def findNumbers(data, target):
    for item in range(len(data)):
        if target == data[item]:
            return item
    return -1;

def findCoordinatesMatrix(Matrix, target):
    for row in range(len(Matrix)):
        for col in range(len(Matrix[row])):
            if Matrix[row][col] == target:
                return (row, col)
    return (-1, -1)
   