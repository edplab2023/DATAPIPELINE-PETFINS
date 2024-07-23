#!/bin/bash

# 압축 해제
unzip docker_project.zip

# Docker 이미지 로드
for tar_file in docker_images/*.tar; do
  echo "Loading $tar_file..."
  docker load -i "$tar_file"
done

cp docker-images/docker-compose.yaml ./docker-compose.yaml
cp docker-images/unzip-docker-compose.sh ./unzip-docker-compose.sh

# Docker Compose 실행
docker-compose up -d