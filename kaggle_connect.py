from kaggle.api.kaggle_api_extended import KaggleApi as ka
import pandas as pd
from pathlib import Path

#"Download" base path
base_folder = Path("./")

#Initialize the API and authenticate
api = ka()
api.authenticate()

#Prompt for the search term
buscar = input("Buscar data: ")