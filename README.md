# siloka-ml-gateway

Siloka-ml-gateway is a consumable REST API service for the [siloka-backend](https://github.com/c22-cb02/siloka-backend) and collaboratively developed by Bangkit Academy 2022 Cohort.

Contributor to this repostory:

- [Dennis Al Baihaqi Walangadi](https://github.com/dnswd)
- [Gita Permatasari Sujatmiko](https://github.com/gpersable)
- [Radhiansya Zain Antriksa Putra](https://github.com/RadhiansyaZ)

## Tech Stacks

This project was built on top of:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Compute Engine](https://console.cloud.google.com/compute/instances)
- [Cloud Storage](https://console.cloud.google.com/storage)
- [Cloud Build](https://console.cloud.google.com/cloud-build/builds)
- [Container Registry](https://console.cloud.google.com/gcr/)
- [Cloud Logging](https://console.cloud.google.com/logs/query)

## Development

1. Install [Poetry](https://python-poetry.org/docs/)
2. Install dependencies
   ```
   poetry install
   ```
3. Create `.env` file and fill it with
   ```
   GOOGLE_APPLICATION_CREDENTIALS='local/path/to/service_account_key.json'
   ```

### Running the Service without Container

```bash
$ poetry run uvicorn app.main:app --reload
```

Or

```bash
$ poetry shell
$ uvicorn app.main:app --reload
```

### Building the Container

```bash
$ docker build -t siloka-ml-gateway .
```

### Running the Container

```bash
$ docker run -d -p 80:80 siloka-ml-gateway
```

## Load the ML model

1. Open main.py and checks
   ```
   GOOGLE_APP_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
   ML_STORAGE_BUCKET = "siloka-ml-resources"
   ```
2. Change `ML_STORAGE_BUCKET` value to match your bucket name where you stored your model.
3. Store your model, tokenizer, and intents in Google Cloud Storage Bucket.
4. Make sure your model, tokenizer, and intents are named with `chatbot-model.h5`, `tokenizer.pickle`, and `intents.json`.
   or
   modify this snippet in main.py according to your needs

   ```python
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
   ```
