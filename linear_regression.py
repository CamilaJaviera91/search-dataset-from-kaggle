import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OrdinalEncoder as oe
from sklearn.linear_model import LinearRegression as lr
from kaggle_connect import kaggle_connect as kc

# Auxiliary functions
def encode_column(df, column_name, ordinal_categories):
    encoder = oe(categories=[ordinal_categories])
    df['new_' + column_name] = encoder.fit_transform(df[[column_name]])
    df.drop(columns=[column_name], inplace=True)
    return df

def get_column_input(df, prompt):
    while True:
        column_name = input(prompt)
        if column_name in df.columns:
            return column_name
        print("Invalid column. Please try again.")


def get_ordinal_categories(column_values):
    """
    Returns unique values sorted if they are ordinal.
    If the order is known beforehand, this function can be customized.
    """
    return sorted(column_values)

def plot_regression(x, y_pred, values, value_media, table_data):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_pred, color='blue', linewidth=2, label='Regression Line')
    plt.scatter(x, y_pred, color='green', label='Predictions')
    plt.xlabel(values)
    plt.ylabel(value_media + ' (Prediction)')
    plt.title('Linear Regression')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.table(cellText=table_data.values,
              colLabels=table_data.columns,
              cellLoc='center', loc='bottom',
              bbox=[0.1, -0.3, 0.8, 0.2])
    plt.subplots_adjust(left=0.1, bottom=0.3)
    plt.show()


#Main
data = kc()
df = pd.DataFrame(data)

# Show the number of unique values per column
print(df.nunique())

# Select column to encode
values = get_column_input(df, "Enter the name of the column to encode: ")
ordinal_categories = get_ordinal_categories(df[values].unique())
data = encode_column(data, values, ordinal_categories)

#Select column to calculate the average
value_media = get_column_input(data, "Enter the name of the columns to average: ")
score_columns = [col for col in data.columns if col.endswith(value_media)]
data[value_media] = round(data[score_columns].sum(axis=1) / len(score_columns))
data.drop(columns=score_columns, inplace=True)