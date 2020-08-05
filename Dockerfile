FROM ubuntu
RUN apt-get update
RUN apt-get -y install python3.7
RUN apt-get -y install python3-pip
COPY ./reqirements.txt .
RUN pip3 install -r ./reqirements.txt
RUN mkdir /home/app
WORKDIR /home/app
COPY . /home/app
ENTRYPOINT ["python3"]
CMD ["main.py"]
