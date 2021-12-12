FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /test_discount_cards

WORKDIR /test_discount_cards

COPY ./requirements.txt /test_discount_cards/requirements.txt
RUN pip install -r requirements.txt

COPY . /test_discount_cards