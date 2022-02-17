from fastapi import FastAPI
import datetime
from pydantic import BaseModel
from typing import Optional
import uvicorn

## Is it normal to do this to force structure
class Person(BaseModel):
    first: str
    last: str
    age: Optional[int] = None

app = FastAPI()

test_dict = {}

# basic test
@app.get('/')
def root():
    return {"message": "Hello World"}

# little more complicated
@app.get('/time')
def get_time():
    return  str(datetime.datetime.now())

# can I return something to myself
@app.get('/test_return/{data}')
def add_data(data):
    return {'test_return': data}


# basic post. Is it normal to use the pydantic BaseModel? 
@app.post('/add_person')
def add_person(person:Person):
    if str(person.first+person.last) not in test_dict.keys():
        test_dict[(person.first+person.last)] = person
    return test_dict

# see who has been added
@app.get('/get_people')
def get_people():
    return test_dict


### RUN PROGRAMMATICALLY
# if __name__ == "__main__":
#     uvicorn.run("main:app") #, host="0.0.0.0", port=5000, log_level="info")