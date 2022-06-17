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
