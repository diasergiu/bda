import pandas as pd

def get_pokemons():
    return pd.read_csv("datasets/Pokemon.csv", encoding="latin-1")

def problem1():
    pokemons = get_pokemons()
    print(pokemons.head(10))
    print(pokemons.tail())


def problem2():
    pokemons = get_pokemons()
    print(pokemons.shape)
    # print(pokemons.columns)
    
def problem3():
    pokemons = get_pokemons()
    print(pokemons.info())
    print(pokemons.columns)
    print(pokemons.dtypes)

def problem4(pokemons):
    pronsSplitLine()
    pokemons = pokemons.rename(columns = {
        "#":       "pokemon_id",
        "Name":    "name",
        "Type 1":  "type_1",
        "Type 2":  "type_2",
        "Total":   "total",
        "HP":      "hp",
        "Attack":  "attack",
        "Defense": "defense",
        "Sp. Atk": "sp_atk",
        "Sp. Def": "sp_def",
        "Speed":   "speed",
        "Stage":   "stage",
        "Legendary": "legendary",
    })
    print(pokemons.columns)


def problem5(pokemons):
    pronsSplitLine()
    pokemons["Type 2"] = pokemons["Type 2"].fillna("None")
    print(pokemons.head(20))


def problem6(pokemons):
    pronsSplitLine()
    print(pokemons.describe())


def problem7(pokemons):
    pronsSplitLine()
    print(pokemons[pokemons["Attack"] == pokemons["Attack"].max()])
    print(pokemons[pokemons["Defense"] == pokemons["Defense"].max()])
    print(pokemons[pokemons["Speed"] == pokemons["Speed"].max()])


def problem8(pokemons):
    pronsSplitLine()
    # result = pokemons[pokemons.groupby("Type 1").sum(), pokemons["Total"].mean().sort_values(ascending=False)]
    result = pokemons.groupby("Type 1")["Total"].mean().sort_values(ascending=False)
    print(result)


def problem9():
    pokemons = get_pokemons()
    pronsSplitLine()
    pokemons["power_score"] = pokemons["Attack"] + pokemons["Defense"] + pokemons["Speed"]
    print(pokemons.sort_values("power_score", ascending=False)[["Name", "Type 1", "power_score"]].head(10))


def pronsSplitLine():
    print("-------------")

if __name__ == "__main__":
    # problem1()
    # problem2()
    # problem3()
    pokemons = get_pokemons()
    # problem4(pokemons)
    # problem5(pokemons)
    # problem6(pokemons)
    # problem7(pokemons)
    problem8(pokemons)
    # problem9()

