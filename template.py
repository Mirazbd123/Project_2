import os 
import pathlib
from  pathlib import Path 
import logging 

#instade of using print function we can use loggin for sowing the massage when we exicute the template.py
#we can use this ling in every thing
logging.basicConfig(level=logging.INFO , format = '[%(asctime)s]: %(message)s:')

projct_name = 'cnn_classifier'

#have to creat a list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"source/{projct_name}/__init__.py",
    f"source/{projct_name}/components/__init__.py",
    f"source/{projct_name}/utils/__init__.py",
    f"source/{projct_name}/config/__init__.py",
    f"source/{projct_name}/config/configuration/__init__.py",
    f"source/{projct_name}/pipeline/__init__.py",
    f"source/{projct_name}/entity/__init__.py",
    f"source/{projct_name}/constants/__init__.py",

    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py"
    "research/trials.ipynb",
    "templates/index.html"


]

#creat a loop for making 
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath , "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
    
    else: 
        logging.info(f"{filename} is already exists")