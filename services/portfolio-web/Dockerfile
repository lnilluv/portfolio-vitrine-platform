FROM node:22-alpine AS build

WORKDIR /app

COPY services/portfolio-web/package.json ./
RUN npm install

COPY services/portfolio-web ./
RUN npm run build

FROM node:22-alpine AS runtime

WORKDIR /app

ENV NODE_ENV=production
ENV PORT=4173

COPY --from=build /app/build ./build
COPY --from=build /app/package.json ./package.json
COPY --from=build /app/node_modules ./node_modules

EXPOSE 4173

CMD ["node", "build/index.js"]
