FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /code/
RUN chmod +x /code/wait_for_it.sh