import pandas as od
import matplotlib.pyplot as plt

from sklearn.preprocessing import OrdinalEncoder as oe
from sklearn.linear_model import LinearRegression as lr
from kaggle_connect import kaggle_connect as kc

#1 Step: Create a new def where it calls the DataFrame
def load_data():
    return kc()