FROM node:alpine

WORKDIR /app

COPY package*.json ./

COPY . .

RUN npm install

RUN npm run build

EXPOSE 5173

CMD ["npm", "run", "start", "--", "--host"]