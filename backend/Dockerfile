# for backend by python3
## latest and slim version
FROM python:3.10.4-slim-buster

# working directry
WORKDIR /usr/src/

# env vars
## ignore .pyc
ENV PYTHONDONTWRITEBYTECODE 1
## ignore stdout and errout in binary
ENV PYTHONUNBUFFERED 1
## abale utf-8
ENV PYTHONUTF8 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependecies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/entrypoint.sh

# waiting for connection db
ENTRYPOINT [ "/usr/src/entrypoint.sh" ]
