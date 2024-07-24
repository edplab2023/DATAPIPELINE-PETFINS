#!/bin/bash

# 1. Docker 이미지를 서비스 이름으로 tar 파일로 저장
echo "Building Docker Compose services..."
docker-compose build

# 서비스 이름 목록 가져오기
services=$(docker-compose config --services)


# 2. Docker Compose 파일 준비
COMPOSE_FILE="docker-compose.yaml"
UNZIP_FILE="unzip-docker-compose.sh"
ENV_FILE=".env"

# 3. 모든 파일을 .zip으로 압축
IMAGES_DIR="docker_images"
ZIP_FILE="docker_project.zip"

docker images

mkdir -p $IMAGES_DIR
docker save $(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'datapipeline') -o $IMAGES_DIR/images.tar

cp $COMPOSE_FILE $IMAGES_DIR/$COMPOSE_FILE
cp $UNZIP_FILE $IMAGES_DIR/$UNZIP_FILE
cp $ENV_FILE $IMAGES_DIR/$ENV_FILE

echo "Compressing files into $ZIP_FILE..."
zip -r $ZIP_FILE $IMAGES_DIR

echo "Compression complete. File saved as $ZIP_FILE."