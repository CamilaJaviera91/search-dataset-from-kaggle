import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OrdinalEncoder as oe
from sklearn.linear_model import LinearRegression as lr
from kaggle_connect import kaggle_connect as kc

# Auxiliary functions

def get_column_input(df, prompt):
    while True:
        column_name = input(prompt)
        if column_name in df.columns:
            return column_name
        print("Invalid column. Please try again.")

#Main
data = kc()
df = pd.DataFrame(data)

# Show the number of unique values per column
print(df.nunique())

# Select column to encode
values = get_column_input(df, "Enter the name of the column to encode: ")