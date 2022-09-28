"""
    ***************************************************
    author: Park Young-woong
    e-mail: pyw5987@gmail.com
    github: https://github.com/queque5987/better-voice-cloning
    ***************************************************
"""
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

import json
import utils

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ColdStart(BaseModel):
    wav : list
    sr : int
    text : str

class WalmStart(BaseModel):
    embed : list
    sr : int
    text : str

@app.get('/')
def index():
    return FileResponse("index.html")

@app.post('/inference-c')
def cold_inference(userinput: ColdStart):
    print("service requested.")
    userinput = userinput.dict()
    wav = userinput["wav"]
    sr = userinput["sr"]
    text = userinput["text"]
    wav = utils.get_wav(wav, sr, text)
    wav_json = json.dumps({
        "wav": wav,
        "sr": sr
    })
    print("done")
    return JSONResponse(wav_json)

@app.post('/inference-w')
def walm_inference(userinput: WalmStart):
    print("service requested.")
    userinput = userinput.dict()
    embed = userinput["embed"]
    sr = userinput["sr"]
    text = userinput["text"]
    wav = utils.get_wav_embedding(embed, sr, text)
    wav_json = json.dumps({
        "wav": wav,
        "sr": sr
    })
    print("done")
    return JSONResponse(wav_json)
