from fastapi import FastAPI

 

app=FastAPI()
@app.get('/')
def index():
    return {'data':{'name':'Riddhi'}}

@app.get('/about')
def about():
    return {'data':'About Page'}