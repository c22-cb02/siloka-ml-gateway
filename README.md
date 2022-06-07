# siloka-ml-gateway

## Development

Create `.env` file and fill it with

```
GOOGLE_APPLICATION_CREDENTIALS='local/path/to/service_account_key.json'
```

### Running the Service without Container

```bash
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
