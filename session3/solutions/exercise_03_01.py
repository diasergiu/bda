# numbers = [1, 2, 3]

# for number in numbers:
#     print(number)


# numbers = [1, 2, 3]
# it = iter(numbers)

# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3


# with open("les_miserables.txt", "r", encoding="utf-8") as file:
#     it = iter(file)
#     for line in it:
#         print(line)

## 1
# def printLineUntill(numLines):
#     with open("les_miserables.txt", "r", encoding="utf-8") as file:
#         it = iter(file)
#         for _ in range(numLines):
#             print(next(it))

# printLineUntill(1)

# # 2

# TEXT_FILE = "les_miserables.txt"
# target = "Jean Valjean"
# found = None
# def findCharacters(target):
#     with open(TEXT_FILE, "r", encoding="utf-8") as file:
#         for line in file:
#             if target in line:
#                 print(line + "found")
#                 break

# findCharacters(target)


# # 3

TEXT_FILE = "les_miserables.txt"
# count = 0

# with open(TEXT_FILE, "r", encoding="utf-8") as file:
#     it = iter(file)
#     for line in it:
#         count += 1

# print(count)


# 4

# def everageLineLength(filePath):
#     with open(filePath, "r", encoding="utf-8") as file:
#         it = iter(file)
#         totalLength = 0
#         count = 0
#         for line in it:
#             totalLength += len(line)
#             count += 1
#         return totalLength / count
    
# print(everageLineLength("les_miserables.txt"))


# TEXT_FILE = "les_miserables.txt"

# with open(TEXT_FILE, "r", encoding="utf-8") as file:
#     lines = file.readlines()

# print(lines[40])


# def non_empty_lines(path):
#     with open(path, "r", encoding="utf-8") as file:
#         for line in file:
#             line = line.strip()
#             if line != "":
#                 yield line


# for line in non_empty_lines("les_miserables.txt"):
#     print(line)
#     break

def non_Empty_Lines(path, target):
    with open(path, "r", encoding="utf-8") as file:
        count = 0
        for line in file:
            if target in line:
                count += 1
        yield count

for line in non_Empty_Lines("les_miserables.txt", "Jean Valjean"):
    print(line)

# #  from profesor 

# def non_empty_lines(path):
#      with open(path, "r", encoding="utf-8") as file:
#          for line in file:
#              line = line.strip()
#              if line != "":
#                  yield line

# count = 0
# target = "Jean Valjean"

# for line in non_empty_lines(TEXT_FILE):
#     if target in line:
#         count += 1

# print(count)