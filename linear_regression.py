import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OrdinalEncoder as oe
from sklearn.linear_model import LinearRegression as lr
from kaggle_connect import kaggle_connect as kc

#Main
data = kc()
df = pd.DataFrame(data)

# Show the number of unique values per column
print(df.nunique())