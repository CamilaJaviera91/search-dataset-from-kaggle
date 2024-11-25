# search-dataset-from-kaggle

## Description

This project is designed to facilitate the search for datasets on **https://www.kaggle.com.** By entering a keyword, you can access a repository that displays various related dataset options, allowing you to select the most suitable one for your needs.

## Project Requirements

### 1. File kaggle_connect.py:
This file requires the following dependencies to function:

· kaggle.api.kaggle_api_extended (imported as KaggleApi): required to interact with the Kaggle API.
· pandas: used for data manipulation and analysis.
· pathlib (imported as Path): useful for handling file and directory paths.

### 2. File linear_regression.py:
This file depends on the following libraries:

· pandas: for data manipulation and analysis.
· matplotlib.pyplot: for creating visualizations and plots.
· numpy: for numerical calculations and matrix operations.
· sklearn.preprocessing (specifically OrdinalEncoder): for encoding categorical variables ordinally.
·sklearn.linear_model (specifically LinearRegression): to implement linear regression models.
· kaggle_connect: an internal module of the project, defined in the kaggle_connect.py file.