# siloka-ml-gateway

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
