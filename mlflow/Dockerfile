ARG FROM_IMAGE=python:3.10-slim

FROM ${FROM_IMAGE}

COPY . .
ENV PROJECT_DIR opt
WORKDIR /${PROJECT_DIR}
RUN pip install mlflow sqlalchemy psycopg2-binary


CMD [ "mlflow", "server", "--backend-store-uri", "/opt/outputs/mlruns", "--default-artifact-root", "/opt/outputs/mlruns", "--host", "0.0.0.0" ]