#!/bin/bash

# Docker 이미지 로드
docker load -i images.tar


# Docker Compose 실행
docker-compose pull
docker-compose up -d --no-build