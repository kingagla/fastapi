from fastapi import FastAPI

app = FastAPI() # instance od our application


@app.get('/hello') # attaching this function to endpoint
def hello_world():
    """Say Hello to:
        - you
        - me""" # will show up in documentation
    return {"message": "Hello World"}


# @app.post('/hello')
# def index2():
#     return "hi"

# run app:  uvicorn main:app --reload
#                uvicorn <fine_name>:<instance_name> --reload