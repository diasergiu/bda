import csv
# 1

# with open("studio_ghibli_movies.csv", "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     first_row = next(reader)
#     print("Header:", header)
#     print("First title (index 1):", first_row[1])

# 2

# with open("studio_ghibli_movies.csv", "r") as file:
#     reader = csv.DictReader(file)
#     first_row = next(reader)
#     print("Columns:", reader.fieldnames)
#     print("First title (key):", first_row["title"])

# 3

# students = [
#     {"name": "Ana", "score": "85", "email": "ana@mail.com"},
#     {"name": "Ben", "score": "", "email": "ben@mail.com"},
#     {"name": "Cara", "score": "91", "email": ""},
# ]
# with open("students_raw.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "score", "email"])
#     writer.writeheader()
#     writer.writerows(students)

# 4

# with open("students_raw.csv", "r") as in_file:
#     reader = csv.DictReader(in_file)
#     fixed_rows = []

#     for row in reader:
#         if row["email"] == "":
#             row["email"] = "unknown@mail.com"
#         fixed_rows.append(row)

# with open("students_fixed.csv", "w", newline="") as out_file:
#     writer = csv.DictWriter(out_file, fieldnames=["name", "score", "email"])
#     writer.writeheader()
#     writer.writerows(fixed_rows)

# Pre exercise

# 1

def read_cvsDict():
    with open("studio_ghibli_movies.csv", "r") as file:
        reader = csv.DictReader(file)
        movies = list(reader)
    return movies

# 2

def printRowYearMissing():
    movies = read_cvsDict()
    for movie in movies:
        if movie["year"] == "":
            print(movie)

# 3

def correctMissingYear():
    movies = read_cvsDict()
    for movie in movies:
        if movie["year"] == "":
            movie["year"] = "198612" # not the correct year
    with open("studio_ghibli_movies.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["movie_id", "title", "year", "director", "music_by", "country", "language"])
        writer.writeheader()
        writer.writerows(movies)

# 4

def findMissingMisuc():
    movies = read_cvsDict()
    for movie in movies:
        if movie["music_by"] == "":
            print(movie)

# 5

def saveCleanData():
    movies = read_cvsDict()
    movies_clean = []
    for movie in movies:
        if movie["movie_id"] != "" and movie["title"] != "" and movie["year"] != "" and movie["director"] != "" and movie["music_by"] != "" and movie["country"] != "" and movie["language"] != "":
            movies_clean.append(movie)
    with open("studio_ghibli_movies_clean.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["movie_id", "title", "year", "director", "music_by", "country", "language"])
        writer.writeheader()
        writer.writerows(movies_clean)