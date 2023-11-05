FROM python:3.10-slim

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python3-opencv

VOLUME ["/app/output"]
VOLUME ["/app/images"]
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip --no-cache-dir install -r requirements.txt

COPY main.py /app/main.py

ENTRYPOINT ["python", "main.py"]

