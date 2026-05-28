import pandas as pd

def getMovies():
    return pd.read_json("datasets/Movies.json")

def firstProblem():
    movies = getMovies()
    for column in movies.columns:
        if movies[column].isnull().any():
            print(column)

def firstProblemB():
    movies = getMovies()
    nullValues = movies[movies.isnull().any(axis=1)]
    print(nullValues)

def secondProblem():
    movies = getMovies()
    print(movies.isnull().sum())
    print("------------------------------")
    print(movies.isnull().sum().sum())

def thirdProblem():
    movies = getMovies()
    missingGenre = movies[movies["Major Genre"].isnull()]
    print(missingGenre[["Title", "Major Genre"]])

def CleanDistributorAndName(movies):
    # movies = getMovies()
    movies[["Major Genre", "Distributor"]].fillna("missing", inplace=True)
    print(movies[["Title", "Major Genre", "Distributor"]])
    

def problem7(movies):
    # movies = getMovies()
    movies["IMDB Rating"].fillna(movies["IMDB Rating"].mean(), inplace=True)
    print(movies[["Title", "IMDB Rating"]])

def problem8(movies):
    # movies["scores"].fillna(movies["scores"].interpolate(), inplace=True)
    # print(movies[["Title", "scores"]])
    movies["scores"] = movies[["IMDB Rating", "Rotten Tomatoes Rating"]].mean(axis=1)
    movies["scores"].fillna(movies["scores"].interpolate(), inplace=True)
    print(movies[["Title", "scores"]])

if __name__ == "__main__":
    # firstProblem()
    # firstProblemB()
    # secondProblem()
    # thirdProblem()
    movies = getMovies()
    CleanDistributorAndName(movies)
    print("------------------------------")
    problem7(movies)
    print("------------------------------")
    problem8(movies)

