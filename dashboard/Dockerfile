ARG FROM_IMAGE=python:3.10.6-slim

FROM python:3.10-slim as build-stage

WORKDIR /tmp
RUN pip install poetry
ENV PATH="${PATH}:/root/.local/bin"

COPY pyproject.toml poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.10-slim

WORKDIR /app

COPY --from=build-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt && \
    apt-get -y update && \
    apt-get -y install \
    apt-utils \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

EXPOSE 8501
VOLUME /data_storage


CMD ["streamlit", "run", "src/main.py" ]