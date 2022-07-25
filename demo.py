from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/")
def 작명():
    return FileResponse('index.html')

'''
@app.get("/data")
def 작명():
    return {'hello' : 1234}

    /docs 접속 시 api 문서를 자동으로 만들어준다.
'''

