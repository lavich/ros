FROM python:3

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip3 install -r requirements.txt

# add app
COPY . /usr/src/app
