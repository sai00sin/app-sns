docker-compose build
docker-compose up -d

docker exec -it backend bash
docker exec -it frontend sh

npx create-nuxt-app nuxtproject



delete mode 100644 frontend/src/nuxtproject/.babelrc
delete mode 100644 frontend/src/nuxtproject/jest.config.js
delete mode 100644 frontend/src/nuxtproject/package-lock.json
delete mode 100644 frontend/src/nuxtproject/test/Logo.spec.js