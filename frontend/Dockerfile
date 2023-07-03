FROM ubuntu:focal

WORKDIR /code

RUN apt update && \
  apt install --no-install-recommends --yes \
  nodejs \
  npm

COPY frontend/package.json package.json
COPY frontend/package-lock.json package-lock.json
RUN npm install
