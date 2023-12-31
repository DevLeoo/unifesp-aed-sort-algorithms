import pandas as pd
from Results.selectionSort import df_index

c = pd.DataFrame({
    "1000": [0.1, 0.1, 0.1],
    "10000": [1, 1, 1],
    "100000": [18, 16, 16],
    "1000000": [190, 192, 218]
}, df_index)


c_inverse = pd.DataFrame({
    "1000": [0.3, 0.2, 0.2],
    "10000": [3, 3, 2],
    "100000": [10, 10, 11],
    "1000000": [91, 92, 93]
}, df_index)


c_almost_sorted = pd.DataFrame({
    "1000": [0.09, 0.09, 0.1],
    "10000": [4, 2, 2],
    "100000": [16, 15, 15],
    "1000000": [168, 165, 177]
}, df_index)

java = pd.DataFrame({
    "1000": [29, 39, 36],
    "10000": [72, 68, 71],
    "100000": [234, 337, 212],
    "1000000": [590, 654, 688]
}, df_index)

java_inverse = pd.DataFrame({
    "1000": [35, 35, 33],
    "10000": [115, 185, 156],
    "100000": [0, 0, 0],
    "1000000": [0, 0, 0]
}, df_index)

java_almost_sorted = pd.DataFrame({
    "1000": [36, 32, 29],
    "10000": [74, 79, 94],
    "100000": [422, 385, 491],
    "1000000": [886, 702, 880]
}, df_index)

python = pd.DataFrame({
    "1000": [1, 1, 2],
    "10000": [24, 35, 31],
    "100000": [393, 449, 410],
    "1000000": [5523, 5327, 6395]
}, df_index)

python_inverse = pd.DataFrame({
    "1000": [3, 2, 1],
    "10000": [24, 22, 26],
    "100000": [313, 308, 308],
    "1000000": [3271, 2849, 2889]
}, df_index)

python_almost_sorted = pd.DataFrame({
    "1000": [5, 3, 5],
    "10000": [17, 24, 28],
    "100000": [260, 334, 299],
    "1000000": [3314, 3029, 3105]
}, df_index)

typescript = pd.DataFrame({
    "1000": [6, 5, 5],
    "10000": [20, 17, 16],
    "100000": [83, 84, 85],
    "1000000": [672, 707, 692]
}, df_index)

typescript_inverse = pd.DataFrame({
    "1000": [24, 26, 24],
    "10000": [0, 0, 0],
    "100000": [0, 0, 0],
    "1000000": [0, 0, 0]
}, df_index)

typescript_almost_sorted = pd.DataFrame({
    "1000": [79, 95, 64],
    "10000": [0, 0, 0],
    "100000": [0, 0, 0],
    "1000000": [0, 0, 0]
}, df_index)
