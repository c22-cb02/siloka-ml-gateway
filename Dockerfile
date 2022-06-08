FROM python:3.9

WORKDIR /src

COPY ./production_requirements.txt /src/production_requirements.txt
COPY ./model /src/model

RUN pip install --no-cache-dir --upgrade -r /src/production_requirements.txt

COPY ./app /src/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
