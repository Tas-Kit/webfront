 FROM python:2
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /webfront
 WORKDIR /webfront
 ADD requirements.txt /webfront/
 RUN pip install -r requirements.txt
 RUN apt-get update
 RUN apt-get install -y gettext
 ADD . /webfront/