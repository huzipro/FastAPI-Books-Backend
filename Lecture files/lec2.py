from fastapi import FastAPI, Request, Header
from typing import Optional
from pydantic import BaseModel

class BookCreateModel(BaseModel):
    title:str
    author:str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Below is a path parameter. Anything after tthe greet/ will be mapped to name. Function greet_user will be called with parameter name = (whatever is in name in app.get)

# @app.get("/greet/{name}")
# async def greet_user(name:str) -> dict:
#     return {"message": f"Hello {name} "}

# If the url  = http://127.0.0.1:8000/greet/user/?name=Kai. Anything after the / will be a query parameter. 
@app.get("/greet/user/")
async def greet_query_user(city:str, name:Optional[str] = 'Kai' ) -> dict:
    if city:
        return {"message": f"Hello {name} from {city}." }
    return {"message": f"Hello {name}." }

@app.post('/create_book')
async def create_book(book_data:BookCreateModel, request:Request ):
    return{"book_name": book_data.title, 
           "book_author": book_data.author,
           "reqinfo": request.url_for}

@app.get('/get_headers')
async def get_headers(
    content_type: str = Header(None),
    app_name:str = Header(None),
    host:str = Header(None)
):
    request_headers = {}
    request_headers['content-type'] = content_type
    request_headers['host'] = host
    return request_headers
