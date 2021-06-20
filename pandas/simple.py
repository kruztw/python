import numpy as np
import pandas as pd

items = ["a", "b", "a", "b"]
arg1 = [1, 2, 3, 4]
arg2 = [5, 6, 7, 8]
table = pd.DataFrame({"col0": items, "col1": arg1, "col2": arg2}, columns=["col0", "col1", "col2"])

print(table)

print()
print(table.groupby("col0").aggregate([sum, np.mean, max, min]))

print()
print(table.groupby("col0").aggregate({"col1": sum, "col2": np.mean}))
