from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

jsonfile = 'visiting.json'

def get_data():
    try:
        with open(jsonfile, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"last": "", "now": ""}

import json

def save_data(data):
    with open(jsonfile, 'w') as file:
        json.dump(data, file, indent=4)


@app.get("/date")
async def putinzzz():
    data = get_data()

    data['last'] = data['now']

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['now'] = current_date

    save_data(data)

    return data