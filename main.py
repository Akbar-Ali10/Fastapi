from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def about():
    return{"message":"Hello my s akbar ali "}

@app.get('/services')
def services():
    return{"message":"This is services page "}

@app.get('/contact')
def contact():
    return{"message":"This is contact page"}