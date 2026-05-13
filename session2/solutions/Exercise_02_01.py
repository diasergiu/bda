import csv

def openCVSDictReader():
    with open("movies_Incomplete.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
# 1 
def nameOfColumns():
    reader = openCVSDictReader()
    print(reader[0].keys()) 

def printMoviesNames():
    reader = openCVSDictReader()
    for row in reader:
        print(row["title"])
# 2
def printFirstNRows(n):
    reader = openCVSDictReader()
    for i in range(n):
        print(reader[i])
# 3
def countMoviesFromCountr(country):
    reader = openCVSDictReader()
    count = 0
    for row in reader:
        if row["country"] == country:
            count += 1
    return count
# 4
def findMovieFromExactGenra(genra):
    reader = openCVSDictReader()
    for row in reader:
        if row["genres"] == genra:
            print(row["title"])
            break

# 5
def findMovieFromGenra(genra):
    reader = openCVSDictReader()
    for row in reader:
        if genra in row["genres"]:
            print(row["title"])
            break

# def main():
#     printMoviesNames()