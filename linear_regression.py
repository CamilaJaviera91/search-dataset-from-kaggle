import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    """
    Prompts the user to input a column name and suggests matches if the input is a substring of column names.
    """
    while True:
        column_name = input(prompt)
        
        # Filter columns containing the entered text
        matching_columns = [col for col in df.columns if column_name in col]
        
        if matching_columns:
            print(f"Columns containing '{column_name}': {matching_columns}")
            
            # Ask the user to select an exact column name from the matches
            selected_column = input("Enter the exact column name from the list above: ")
            if selected_column in df.columns:
                return selected_column
            else:
                print("Invalid selection. Please choose a column from the list.")
        else:
            print(f"No columns found containing '{column_name}'. Please try again.")



def get_ordinal_categories(column_values):
    """
    Returns unique values sorted if they are ordinal.
    If the order is known beforehand, this function can be customized.
    """
    return sorted(column_values)

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
value_media = input("Enter the name of the columns to average: ")
score_columns = [col for col in data.columns if col.endswith(value_media)]
data[value_media] = round(data[score_columns].sum(axis=1) / len(score_columns))
data.drop(columns=score_columns, inplace=True)

# Linear regression model
x = data[['new_' + values]]
y = data[value_media]

model = lr()
model.fit(x, y)
y_pred = model.predict(x)

# Create a DataFrame for the table data
unique_values = x['new_' + values].unique()

table_data = pd.DataFrame({
    values: x.values.flatten(),  # Unique values of the encoded column
    value_media+'_prediction': y_pred.round(1)  # Predicted values
})

sorted_table= table_data.sort_values(by=values, ascending=True).drop_duplicates()

value_names = []

# Iterate over each unique value in the 'values' column of the sorted table.
for idx, i in enumerate(sorted_table[values]):
    a = input(f"Enter a value for element {idx} (current: {i}): ")
    value_names.append(a)

#Plot the data and the regression line
plt.plot(x, y_pred, color='red', linewidth=2, label='Regression Line')

# Step 4: Add points on the regression line
plt.scatter(x, y_pred, color='red', label='Points on the Regression Line')

# Create an example table with additional information
# You can use your own data or relevant statistics
table_data_d = {
    'Value': sorted_table[values], 
    'Description': value_names,
    'Prediction': sorted_table[value_media+'_prediction']
}

# Convert the dictionary into a DataFrame for easier handling
df_table = pd.DataFrame(table_data)

# Add the table to the plot, below the x-axis
table = plt.table(cellText=df_table.values,
                  colLabels=df_table.columns,
                  cellLoc='center',
                  loc='bottom',
                  bbox=[0.1, -0.3, 0.8, 0.2])  # [x, y, width, height] to adjust position and size

# Adjust layout to prevent the table from overlapping with the plot
plt.subplots_adjust(left=0.1, bottom=0.3)

plt.xlabel(values)
plt.ylabel(value_media+'_prediction')
plt.title("Linear Regression")
plt.legend()
plt.show()