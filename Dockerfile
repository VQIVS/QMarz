# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /Qmarz

COPY requirements.txt /Qmarz
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /Qmarz

ENTRYPOINT ["python3"]
CMD ["./app/bot/bot.py"]
