### Session 2 | Part 3

> In Part 3, you first learn the cleaning pattern with one tiny dictionary, then apply the same logic to a real CSV dataset as an exercise.

#### 1. Goal

You will learn this exact sequence:

1. create data with a missing value
2. detect what is missing
3. update/fix the missing value
4. save cleaned data to disk

Then you will apply the same flow on `studio_ghibli_movies.csv`.

#### 2. Mini tutorial

Create:

```txt
session2/solutions/exercise-02-02.py
```

Start with two records:

- one missing `music_by`
- one missing `year`

```python
movies = [
    {
        "title": "Howl's Moving Castle",
        "year": "2004",
        "director": "Hayao Miyazaki",
        "music_by": "",
    },
    {
        "title": "Kiki's Delivery Service",
        "year": "",
        "director": "Hayao Miyazaki",
        "music_by": "Joe Hisaishi",
    },
]
```

#### 3. Find the missing value

```python
for i, movie in enumerate(movies, start=1):
    for key, value in movie.items():
        if value.strip() == "":
            print(f"Record {i} missing field: {key}")
```

> [!TIP]
>
> `strip()` is a Python string method that removes extra characters from the beginning and end of a string. For example `text = "   hello   "` with `text.strip()` it becomes `hello`. Use the strip as a general rule of thumb when working with text.

Expected output:

```txt
Record 1 missing field: music_by
Record 2 missing field: year
```

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n * m), where `n` is number of records and `m` is number of fields per record.
>
> Space: O(1) extra space.
>
> </details>

Can you do it better for this specific dataset? Yes.

If you already know the fields you care about (`year`, `music_by`), you can avoid looping through every key:

```python
for i, movie in enumerate(movies, start=1):
    if movie["music_by"].strip() == "":
        print(f"Record {i} missing field: music_by")
    if movie["year"].strip() == "":
        print(f"Record {i} missing field: year")
```

> [!TIP]
>
> What are the time and space complexities of this improved script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n), because each record is checked once with constant work.
>
> Space: O(1) extra space.
>
> </details>

#### 4. Fix the missing value (update dictionary)

```python
if movies[0]["music_by"].strip() == "":
    movies[0]["music_by"] = "Joe Hisaishi"

if movies[1]["year"].strip() == "":
    movies[1]["year"] = "1989"

print(movies)
```

This is the core cleaning idea: detect then update.

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(1) for this exact two-record example.
>
> Space: O(1) extra space.
>
> In a generalized loop across `n` records, update time becomes O(n).
>
> </details>

#### 5. Keep a copy for safekeeping

Sometimes we want both versions:

- raw/original data (unchanged)
- cleaned data (updated)

Naming note:

- `original_movies`: backup copy for safekeeping (do not edit this)
- `cleaned_movies`: working copy that we edit during cleaning

```python
original_movies = [movie.copy() for movie in movies]
cleaned_movies = [movie.copy() for movie in movies]

if cleaned_movies[0]["music_by"].strip() == "":
    cleaned_movies[0]["music_by"] = "Joe Hisaishi"

if cleaned_movies[1]["year"].strip() == "":
    cleaned_movies[1]["year"] = "1989"

print("Original:", original_movies)
print("Cleaned:", cleaned_movies)
```

From this point onward, "cleaned data" means the `cleaned_movies` list.

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n * m), because each copied record copies its fields.
>
> Space: O(n * m), because we store two copied lists.
>
> </details>

#### 6. Save cleaned dictionary to disk

Use JSON for this mini example:

```python
import json

with open("movies_clean.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)

print("Saved: movies_clean.json")
```

Now you have completed the full cleaning pipeline.

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n * m), because writing depends on number of records and fields.
>
> Space: O(1) extra space (excluding data already in memory).
>
> </details>

#### 7. Exercise: apply same logic to CSV dataset

Use: [Birkbeck/studio_ghibli_movies](https://huggingface.co/datasets/Birkbeck/studio_ghibli_movies)

Download:

```bash
hf download Birkbeck/studio_ghibli_movies studio_ghibli_movies.csv \
  --repo-type dataset \
  --local-dir .
```

Expected file in `session2/`:

```txt
studio_ghibli_movies.csv
```

#### 8. Exercise tasks

In `session2/solutions/exercise-02-02.py`, do the following:

1. Load the `studio_ghibli_movies.csv` dataset with `csv.DictReader`.
2. Find missing values by column and print where they are (line number + movie title).
3. Fix missing values (for this dataset, check `year` and `music_by`).
4. Calculate:

   - average of `year`
   - how many times Miyazaki appears as director

5. Save cleaned rows into a new file:

   - `studio_ghibli_movies_clean.csv`

6. Re-check missing values after cleaning and print remaining missing count.

7. What are the time and space complexities of your full script?

<<<<<<< HEAD
#### 9. Quiz
=======

nums = [2, 5, 8, 12, 16, 23, 38, 56, 72]
print(binary_search(nums, 23))  # 5
```

> [!TIP]
>
> Why is binary search `O(log n)`?
>
> <details>
>   <summary>Show answer</summary>
>
> At each step, it removes half of the remaining search space.
> Repeated halving gives logarithmic growth.
>
> </details>

> [!TIP]
>
> What happens if the list is not sorted?
>
> <details>
>   <summary>Show answer</summary>
>
> Binary search can return wrong results because its left/right decisions
> assume sorted order.
>
> </details>

#### 5. Example 2: Merge sort shape (`O(n log n)`)

File: `session2/solutions/exercise-02-03.py`

```python
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


print(merge_sort([7, 2, 9, 1, 5, 3]))
```

> [!TIP]
>
> Why is merge sort `O(n log n)`?
>
> <details>
>   <summary>Show answer</summary>
>
> The recursion depth is about `log n`, and each level processes about `n`
> total elements during merge steps.
>
> </details>

#### 6. Example 3: Nested loop count (`O(n^2)`)

File: `session2/solutions/exercise-02-03.py`

```python
def count_pairs(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                count += 1
    return count


print(count_pairs([10, 20, 30, 40]))
```

> [!TIP]
>
> Why is this `O(n^2)`?
>
> <details>
>   <summary>Show answer</summary>
>
> For each outer-loop item (`n` choices), the inner loop also scans about `n`
> items.
>
> </details>

#### 7. Example 4: Fibonacci recursion (`O(2^n)`)

File: `session2/solutions/exercise-02-03.py`

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(6))
```

> [!TIP]
>
> Why does this grow close to `O(2^n)`?
>
> <details>
>   <summary>Show answer</summary>
>
> Most calls branch into two more calls, creating an exponential recursion tree.
>
> </details>

#### 8. Example 5: Permutation count (`O(n!)` concept, `O(n * n!)` in this implementation)

File: `session2/solutions/exercise-02-03.py`

```python
def permute_count(data):
    if len(data) <= 1:
        return 1

    total = 0
    for i in range(len(data)):
        rest = data[:i] + data[i + 1:]
        total += permute_count(rest)
    return total


print(permute_count([1, 2, 3, 4]))  # 24
```

> [!TIP]
>
> Why is this `O(n!)`?
>
> <details>
>   <summary>Show answer</summary>
>
> It explores every possible ordering (permutation), and there are `n!`
> permutations. In this exact code, repeated list slicing adds extra linear
> work, so a tighter bound is closer to `O(n * n!)`.
>
> </details>

#### 9. Exercise

Add your answers to:

```txt
session2/solutions/exercise-02-03.py
```

Tasks:

1. Run each example with a small input and note the output.
2. For each example, write one sentence explaining the complexity.
3. Modify `binary_search` to count how many loop iterations it performs.
4. Modify `count_pairs` so the inner loop starts from `i + 1`; explain the effect.
5. In a short note, rank these growth rates from smallest to largest:
   `O(log n)`, `O(n log n)`, `O(n^2)`, `O(2^n)`, `O(n!)`.
<!-- They are in order from left to right, smallest to largest -->
#### 10. Quiz

Before starting the quiz, please review the [computational complexity cheatsheet](./session-02-cheatsheet.md).
>>>>>>> 5702c8d (week1 week2)

Complete the following quiz:

```bash
quizmd quizzes/python-dict-cleaning-theory-coding-quiz.md
```
