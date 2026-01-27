""" 
FastAPI uses top-down approach
So whenever using a static and dynamic route, always put static route on top especially when they share the same prefix.
For example, /blog/about should be on top of /blog/{id}
"""

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body:  str
    published: bool

@app.post('/blog')
def create_blog(blog: Blog):
    return blog


@app.get("/")
def index():
    return {'message': [{'kam':'programming'}, {'role':'dev'}]}
    # return "hello world!"

@app.get("/blog")
def about():
    return {'message': 'about page me a gya', 'status': 200, 'data': ['bak', 'lol', 'dev']}


@app.get("/blog/unpublished")
def unpublished():
    return {'message': 'all unpublished blogs'}


# dynamic routing i.e. {id}
@app.get("/blog/{id}")
def blog(id: int):
    return {'message': f'ID is {id}'}

# ON 46min