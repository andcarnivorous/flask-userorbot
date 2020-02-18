FROM ubuntu

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python3-pip

COPY . /workspace

RUN pip3 install -r /workspace/requirements.txt

WORKDIR /workspace

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]