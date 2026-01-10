from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'message': [{'kam':'programming'}, {'role':'dev'}]}
    # return "hello world!"

@app.get("/about")
def about():
    return {'message': 'about page me a gya', 'status': 200, 'data': ['bak', 'lol', 'dev']}