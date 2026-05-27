import pandas as pd

movies = pd.read_json("datasets/Movies.json")

# print(movies.shape)
# print("--------------------")
# print(movies.columns)
# print("--------------------")
# print(movies.dtypes)


# rows = movies.shape[0]
# columns = movies.shape[1]

# print(rows)
# print(columns)


# print(movies.describe())



# print(movies["Production Budget"].mean())
# print(movies["Production Budget"].min())
# print(movies["Production Budget"].max())



# print(movies["Title"])

print(movies["Major Genre"].value_counts())