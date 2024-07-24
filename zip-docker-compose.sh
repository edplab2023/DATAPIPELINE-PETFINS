#!/bin/bash

# 1. Docker 이미지를 서비스 이름으로 tar 파일로 저장
echo "Building Docker Compose services..."
docker-compose build

# 서비스 이름 목록 가져오기
services=$(docker-compose config --services)

# 이미지 tar 파일로 저장
mkdir -p docker_images

# 이미지 목록 확인
docker images

for service in $services; do
  # 서비스에 대한 이미지 이름 가져오기
  image_name=$(docker-compose config | awk '/image:/{print $2}' | grep -E "^${service}\b" | head -n 1)

  if [ -z "$image_name" ]; then
    # 이미지 이름이 없는 경우 서비스 이름을 이미지 이름으로 설정
    image_name=${service}
  fi

  # 이미지 ID 가져오기
  image_id=$(docker images -q $image_name)

  if [ -n "$image_id" ]; then
    echo "Saving image for service $service as $image_name.tar"
    docker save -o docker_images/${image_name}.tar $image_id
  else
    echo "Image id = $image_id"
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