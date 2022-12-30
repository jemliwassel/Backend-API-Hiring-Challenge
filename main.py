import json
from typing import List
from uuid import UUID, uuid4
from fastapi import Depends, FastAPI, File, Form, HTTPException, Response, UploadFile
import pandas as pd
import matplotlib.pyplot as plt
import io



from models import Dataset

app = FastAPI()

datasets = {}  # dictionary to store filenames
data = {} ; # dictionary to store uploaded datasets, with the id as the key and the dataset as the value


def get_dataset(id: int):
    if id not in data:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return datasets[id]













    

