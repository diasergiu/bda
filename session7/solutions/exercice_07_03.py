import numpy as np
import pandas as pd

def get_array():
    return np.array([2,5,7,9,11,14,17,21])


def problem3():
    arr = get_array()
    print(arr)
    print(arr.shape)
    print(arr.dtype)

def problem4():
    arr = get_array()
    print(arr.mean())
    print(arr.min())
    print(arr.max())
    print(arr.std())


def problem5():
    arr = get_array()
    score_plus10 = arr + 10
    print(score_plus10)
    biggerThan = score_plus10 > 20
    print(biggerThan)
    print(score_plus10[biggerThan])


def problem6():
    arr = get_array()
    even_numbers = arr % 2 == 0
    second_even_numbers = arr[arr % 2 == 0]
    print(arr[even_numbers])
    print(second_even_numbers)

def get_matrix():
    return np.array([[1,2,3],[4,5,6],[7,8,9]])

def problem7():
    matrix = get_matrix()
    print(matrix)
    print(matrix.shape)
    print(matrix[0,:])
    print(matrix[:, 1])

def get_pokemons():
    return pd.read_csv("datasets/Pokemon.csv", encoding="latin-1")


def problem8():
    pokemons = get_pokemons()
    attacks = pokemons["Attack"]
    print(attacks.mean())
    print(attacks.min())
    print(attacks.max())
    print("-------------")
    print(attacks[attacks > 120])
    print("------------- second iteration")
    print(pokemons[pokemons["Attack"] > 120][["Name", "Attack"]])
    print("the differance between the tow is that we can use this library to get values")


if __name__ == "__main__":
    # problem3()
    # problem4()
    # problem5()
    # problem6()
    # problem7()
    problem8()