FROM node:12.13-alpine

WORKDIR /app
COPY ./frontend /app

RUN apk update
RUN npm install -g npm && \
    npm install --save nuxt && \
    yarn add --dev jest

ENV HOST 0.0.0.0
EXPOSE 3000