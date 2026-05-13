import csv

def OpenCVS():
    with open("movies.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def printGenres():
    with open("movies.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 4:
                print(row[4])

def printFirstRow():
    with open("movies.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        firstRow = next(reader)
        for colm in firstRow:
            print(colm)
        # first_row = next(reader)
        # print(first_row)

def printProblem2(number):
    with open("movies.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in range(0, number):
            print(next(reader))

def printProblem3():
    with open("movies.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 4 and row[4] == "Action":
                print(row)
                break


def printProblemExersie2():
    with open("movies.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        expected_columns = len(next(reader))
        index = 0;
        for row in enumerate(reader):
            index += 1
            if len(row) != expected_columns:
                print("Issue at row: " + str(index) + " :")