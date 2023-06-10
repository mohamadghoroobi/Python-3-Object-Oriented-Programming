import pickle

some_data = [
    "a list",
    "containing",
    5,
    "values including another list",
    [["inner"], ["list"]]
]

with open ("pickled_list", "wb") as file:
    pickle.dump(some_data, file)