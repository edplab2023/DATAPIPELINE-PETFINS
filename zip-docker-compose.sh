#!/bin/bash

# 1. Docker 이미지를 서비스 이름으로 tar 파일로 저장
echo "Building Docker Compose services..."
docker-compose build

# 서비스 이름 목록 가져오기
services=$(docker-compose config --services)

# 이미지 tar 파일로 저장
mkdir -p docker_images

for service in $services; do
  # 이미지 ID 및 이미지 이름 가져오기
    image_name=$(docker-compose config | awk '/image:/{print $2}' | grep -E "^${service}\b" | head -n 1)

  if [ -n "$image_id" ]; then
    # 이미지 이름: 서비스 이름 사용
    image_name="$service"

    echo "Saving image for service $service as $image_name.tar"
    docker save -o docker_images/{image_name}.tar $image_id
  else
    echo "No image found for service $service"
  fi
done

# 2. Docker Compose 파일 준비
COMPOSE_FILE="docker-compose.yaml"
UNZIP_FILE="unzip-docker-compose.sh"
ENV_FILE=".env"

# 3. 모든 파일을 .zip으로 압축
IMAGES_DIR="docker_images/"
ZIP_FILE="docker_project.zip"

cp $COMPOSE_FILE $IMAGES_DIR$COMPOSE_FILE
cp $UNZIP_FILE $IMAGES_DIR$UNZIP_FILE
cp $ENV_FILE $IMAGES_DIR$ENV_FILE

echo "Compressing files into $ZIP_FILE..."
zip -r $ZIP_FILE $IMAGES_DIR

echo "Compression complete. File saved as $ZIP_FILE."