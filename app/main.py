import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from .ml_model import predict_sentences
from .utils import download_blob_from_bucket, load_file, load_model, load_tokenizer


load_dotenv()
GOOGLE_APP_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
ML_STORAGE_BUCKET = "siloka-ml-resources"

# Download latest ml resources
download_blob_from_bucket(
    ML_STORAGE_BUCKET, "chatbot-model.h5", "model/chatbot-model.h5"
)
download_blob_from_bucket(
    ML_STORAGE_BUCKET, "tokenizer.pickle", "model/tokenizer.pickle"
)
download_blob_from_bucket(ML_STORAGE_BUCKET, "intents.json", "model/intents.json")

model = load_model("./model/chatbot-model.h5")
tokenizer = load_tokenizer("./model/tokenizer.pickle")
intents = load_file("./model/intents.json")

# Take every tag labels from intents
labels = [obj["tag"] for obj in intents["intents"]]

# Create a responses dictionary based on it's tag
responses = {obj["tag"]: obj["responses"][0] for obj in intents["intents"]}


class MessagesReq(BaseModel):
    messages: str


app = FastAPI()

origins = ["*"]

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
    PADDING = "post"
    MAXLEN = 15

    predicted_tag, tag_percentage = predict_sentences(
        [req.messages], model, tokenizer, labels, PADDING, MAXLEN
    )
    predicted_response = responses[predicted_tag]

    return {
        "tag": predicted_tag,
        "accuracy": float(tag_percentage),
        "predicted_response": predicted_response,
    }
