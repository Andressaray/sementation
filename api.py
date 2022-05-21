from fastapi import FastAPI
from pydantic import BaseModel
import sementacion as s
from fastapi.middleware.cors import CORSMiddleware
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
@app.get("/")
@app.post("/text")
def tranformWord(info: Info):
  print(info)
  se = s.main(info.text)
  return { 
    'status': 200,
    'body': {
      # se.list_words,
      # se.bag_words
    }
  }
