from kaggle.api.kaggle_api_extended import KaggleApi as ka
import pandas as pd
from pathlib import Path

#"Download" base path
base_folder = Path("./")

#Initialize the API and authenticate
api = ka()
api.authenticate()

#Prompt for the search term
search_term = input("Search for data: ")

#List datasets related to the search term
datasets = api.dataset_list(search=search_term)

for dataset in datasets:
    print("Dataset found:", dataset.ref)

#Dataset selection
data_ref = input("Enter Option (dataset ref): ")

# Destination folder for the download
new_folder = input("Enter the name of the new folder to store the dataset: ")
download_path = base_folder / new_folder
