import pandas as pd
from selectionSort import df_index

c = pd.DataFrame({
    "1000": [0.1, 0.1, 0.1],
    "10000": [1, 1, 1],
    "100000": [18, 16, 16],
    "1000000": [190, 192, 218]
}, df_index)

