FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "ner_service:app", "--host", "0.0.0.0", "--port", "8000" ]

EXPOSE 8000
