import csv
# 1
def openCSVFile():
    with open("movies.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)
# 2
def printRowCoumnNumber():
    reader = openCSVFile()
    index = 0
    for row in reader:
        print("Row " + str(index) + " has " + str(len(row)) + " columns")
        index += 1

def printNumberOfRowsCoulmns():
    reader = openCSVFile()
    rowCount = 0
    columnCount = 0
    for row in reader:
        rowCount += 1
        columnCount += len(row)
    print("The file has " + str(rowCount) + " rows and " + str(columnCount) + " columns")

# 3
def printRowsFromNumber(numRows):
    reader = openCSVFile()
    for row in range(numRows):
        print(reader[row])

# 4
def movieByGenre(genre):
    reader = openCSVFile()
    findMovie = False
    for row in reader:
        for column in range(3, 5, 1):
            if genre == row[column]:
                print(row)
                findMovie = True
        if findMovie:
            break

# 5
def printAverageRating():
    reader = openCSVFile()
    sizeFile = len(reader) - 1
    ratingSum = 0
    for row in range(1, len(reader)):
        numInteger = 0
        for column in reader[row]:
            if column.isdigit():
                numInteger += 1
            if numInteger == 3:
                ratingSum += float(reader[row][2])
    print("The average rating for all movies is " + str(ratingSum / sizeFile))
        

def printAverageRating(genre):
    reader = openCSVFile()
    ratingSum = 0
    movieCount = 0
    for row in reader:
        isGenre = False
        for column in range(3, 5, 1):
            if genre == row[column]:
                ratingSum += float(row[2])
                movieCount += 1
    if movieCount > 0:
        print("The average rating for " + genre + " movies is " + str(ratingSum / movieCount))
    else:
        print("No movies found for genre: " + genre)