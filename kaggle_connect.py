from kaggle.api.kaggle_api_extended import KaggleApi as ka
import pandas as pd
from pathlib import Path

def kaggle_connect():

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

    #Destination folder for the download
    new_folder = input("Enter the name of the new folder to store the dataset: ")
    download_path = base_folder / new_folder

    #Create the folder if it doesn't exist
    download_path.mkdir(parents=True, exist_ok=True)

    #Download the dataset and unzip it in the specified folder
    api.dataset_download_files(data_ref, path=str(download_path), unzip=True)

    #List all CSV files in the download directory
    csv_files = list(download_path.glob('*.csv'))
    if not csv_files:
        print("No CSV files found in the dataset.")
    else:
        #Select the first CSV file in the directory
        csv_file = csv_files[0]

    #Load the dataset into a DataFrame
        df = pd.read_csv(csv_file)
    
    return df

kaggle_connect()