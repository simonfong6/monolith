# Build the react app.
FROM node:12.18.2 as builder

WORKDIR /code

COPY ./frontend/frontend /code

RUN npm install
RUN npm run build

FROM ubuntu:focal

ENV FLASK_APP ./app/backend/server.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development
ENV MONGO_HOST localhost
ENV MONGO_USERNAME root
ENV MONGO_PASSWORD example
ENV MONGO_DATABASE example_dev

# Copy the frontend build from the node image.
COPY --from=builder /code/build /code/build

WORKDIR /code

RUN apt-get update && \
  apt-get install --no-install-recommends --yes \
  python3 \
  python3-pip

COPY . /code

RUN pip3 install ./app

CMD ["flask", "run"]
