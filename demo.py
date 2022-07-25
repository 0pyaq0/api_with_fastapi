from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def 작명():
    return 'hello'

@app.get("/data")
def 작명():
    return {'hello' : 1234}
