from fastapi import FastAPI
from pydantic import BaseModel
import sementacion as s
from fastapi.middleware.cors import CORSMiddleware
import json

class Info(BaseModel):
  text : str

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.post("/text")
def tranformWord(info: Info):
  se = s.main(info.text)
  print(se)
  # text = se.cleanTweets(info.text)
  return { 'status': 200, 'text': se }
