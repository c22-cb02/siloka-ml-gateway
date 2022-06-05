from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .ml_model import predict_sentences
from .utils import load_model, load_tokenizer

class MessagesReq(BaseModel):
    messages: str

app = FastAPI()

model = load_model('./model/chatbot-model.h5')
tokenizer = load_tokenizer('./model/tokenizer.pickle')

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello Bangkit"}

@app.post("/predict/")
async def predict_label(req: MessagesReq):
    PADDING = 'post'
    MAXLEN = 15

    result = predict_sentences([req.messages], model, tokenizer, PADDING, MAXLEN)

    return {"label": result}