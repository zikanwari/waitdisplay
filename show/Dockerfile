FROM php:apache

COPY html /var/www/html

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && apt-get clean && rm -rf /var/lib/apt/lists/*
