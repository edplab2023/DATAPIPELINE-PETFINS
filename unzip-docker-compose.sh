#!/bin/bash

# Docker 이미지 로드
for tar_file in *.tar; do
  echo "Loading $tar_file..."
  docker load -i "$tar_file"
done

# Docker Compose 실행
docker-compose up -d