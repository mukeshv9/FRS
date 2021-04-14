FROM ubuntu

RUN apt-get update && apt-get install python3.7
RUN apt-get install python3-pip -y

RUN pip3 install starlette uvicorn google aiofiles jinja2 pymongo python-multipart

COPY . /opt/app
WORKDIR /opt/app

CMD [ "python3", "app.py", "serve" ]