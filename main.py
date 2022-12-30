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

@app.get("/datasets/")
async def list_datasets():
    data1 = {}
    for id in data : 
        df = data[id]
        res = df.to_json(orient="records")
        parsed = json.loads(res)
        data1[id] = parsed   #Dictionary of datasets 
    return data1
       
@app.post("/datasets/")
async def create_dataset(csv_file: UploadFile = File(...)):
    try: 
        df = pd.read_csv(csv_file.file)
        id = len(data)  # use the number of datasets as the id for the new dataset
        data[id] = df
        datasets[id] = csv_file
    except Exception as e:
        raise HTTPException(status_code=400, detail= "Unable to read CSV file")
    return {"id": id}

@app.get("/datasets/{id}/")
def get_dataset_info(id: int, dataset = Depends(get_dataset)):
        return {"filename": dataset, "size": len(data[id])}
    
















    

