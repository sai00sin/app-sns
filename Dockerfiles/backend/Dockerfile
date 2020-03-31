FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./Dockerfiles/backend/requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./backend /code