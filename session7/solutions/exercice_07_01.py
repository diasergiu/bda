import pandas as pd

def getMovies():
    return pd.read_json("datasets/Movies.json")

def firstProblem():
    movies = getMovies()
    print(movies.head())
    print(movies.tail())
    print(movies.shape)


def secondProblem():
    movies = getMovies()
    print(movies.dtypes)
    movieStatistics = movies.dtypes.nunique()
    print("------------------------------")# to do statictics for numeric columns only
    print(movieStatistics)

def thirdProblem():
    movies = getMovies()
    print(movies[["Title", "Release Date", "IMDB Rating"]])

def fourthProblem():
    movies = getMovies()
    high_rated = movies[movies["IMDB Rating"] >= 8]
    print(high_rated)


def fifthProblem():
    movies = getMovies()
    movies["Long Movies"] = movies["Running Time min"] > 120
    print(movies["Long Movies"])


def sixthProblem():
    movies = getMovies()
    print(movies["Major Genre"].value_counts())


def seventhProblem():
    movies = getMovies().sort_values(by="IMDB Rating", ascending=True)
    print(movies)


if __name__ == "__main__":
    # firstProblem()
    # secondProblem()
    # thirdProblem()
    # fourthProblem()
    # fifthProblem()
    # sixthProblem()
    seventhProblem()