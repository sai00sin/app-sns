FROM node:12.13-alpine

WORKDIR /usr/src/app
COPY ./frontend /usr/src/app

RUN apk update
RUN npm install -g npm && \
    npm install --save nuxt && \
    yarn add --dev jest

ENV HOST 0.0.0.0
EXPOSE 3000