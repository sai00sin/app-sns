FROM node:10.14.1-alpine

WORKDIR /app

RUN apk update && \
    npm install -g npm && \
    npm install -g create-nuxt-app

ENV HOST 0.0.0.0
EXPOSE 3000