FROM tiangolo/uvicorn-gunicorn:python3.8-slim

ADD . /app
WORKDIR /app
COPY . /app

##
RUN apt update && apt -y dist-upgrade
RUN apt -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 gcc python3-dev python3-dev python3-pip cython3 curl
RUN apt install -y netcat-traditional

COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install pydantic[email]