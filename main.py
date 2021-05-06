from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# --------Creating Instance app----------
app = FastAPI()

# -----------simple route-------------
@app.get('/')
def index():
    return {'data': {
        'cook_time':'50m', 
        'img':'',
        'ingredients':[''],
        'prep_time':'4h',
        'steps':[''],
        'title':'Pizza',
        }}

@app.get('/about')
def about():
    return "This is about page"


# passing id into route
@app.get('/about/{id}')
def show(id:int):
    # fetch id = id
    return {'data': id}


# passing id pluse route
@app.get('/about/{id}/comments')
def comments(id):
    # fetch comments of recipie with id = id   
    return {'data':'This is comment of id'}


#-----Query parameter example /blog?limit=10&publish=true
@app.get('/blog')
# to give default value in route - def blog(limit=10, publish : bool=True):
# Example of optional parameter in route - def blog(limit, publish : bool, sort:Optional[str] = None):
def blog(limit, publish : bool):
    if publish:
        return {'data':f'{limit} blog'}
    else:
        return {'data':'no published blogs'}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# To run code use this command -- uvicorn folder_name.main:app --reload