# search-dataset-from-kaggle

## Description
This project is designed to facilitate the search for datasets on **https://www.kaggle.com.** By entering a keyword, you can access a repository that displays various related dataset options, allowing you to select the most suitable one for your needs.<br>

## Prerequisites

Before you begin, make sure you have the following installed:<br>

- Python 3.8 or higher<br>
- Pip (Python package manager)<br>

## Project Requirements

### 1. File kaggle_connect.py:
This file requires the following dependencies to function:<br>

- **kaggle.api.kaggle_api_extended** (imported as **KaggleApi**): required to interact with the Kaggle API.<br>
- **pandas**: used for data manipulation and analysis.<br>
- **pathlib** (imported as **Path**): useful for handling file and directory paths.<br>

### 2. File linear_regression.py:
This file depends on the following libraries:<br>

- **pandas:** for data manipulation and analysis.<br>
- **matplotlib.pyplot:** for creating visualizations and plots.<br>
- **numpy:** for numerical calculations and matrix operations.<br>
- **sklearn.preprocessing** (specifically **OrdinalEncoder**): for encoding categorical variables ordinally.<br>
- **sklearn.linear_model** (specifically **LinearRegression**): to implement linear regression models.<br>
- **kaggle_connect**: an internal module of the project, defined in the **kaggle_connect.py** file.<br>

## Project Features

- Search for and download a **relevant dataset from Kaggle**.<br>
- Select a **descriptive variable** from the dataset for **analysis.**<br>
- **Calculate the average** of the selected values as a statistical measure.<br>
- Create a **line chart** to visualize the relationship between two variables **(X, Y)**.