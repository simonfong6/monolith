FROM ubuntu:focal

WORKDIR /code

RUN apt-get update && \
  apt-get install --no-install-recommends --yes \
  python3 \
  python3-pip

COPY . /code

RUN pip3 install .

CMD ["flask", "run"]
