from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
app = FastAPI()

class Model(BaseModel):
    name : str
    phone : int

@app.get("/")
def 작명():
    return FileResponse('index.html')

'''
@app.get("/data")
def 작명():
    return {'hello' : 1234}

    /docs 접속 시 api 문서를 자동으로 만들어준다.
'''

@app.post("/send")
def 작명(data : Model):
    print(data)
    return '전송 완료'