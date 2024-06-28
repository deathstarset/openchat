FROM node:20.14.0-alpine AS build

WORKDIR /frontend

COPY package.json package-lock.json ./

RUN npm install

COPY . .
ARG MODE=prod
RUN npm run build -- --mode ${MODE}

EXPOSE 4173

CMD ["npm", "run", "preview"]