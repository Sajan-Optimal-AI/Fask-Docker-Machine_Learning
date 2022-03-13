#FROM ubuntu:latest
#RUN apt-get update
#RUN apt-get install python3-pip
#COPY . /usr/app
#EXPOSE 8000
#WORKDIR /usr/app/
#RUN pip3 install -r requirements.txt
#CMD python flaskapi_flasgger.py


FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install Flask && \
    pip3 install flasgger && \
    pip3 install pandas && \
    pip3 install numpy && \
    pip3 install scikit-learn 


COPY . /usr/app
EXPOSE 8000
WORKDIR /usr/app/


CMD python3 flaskapi_flasgger.py