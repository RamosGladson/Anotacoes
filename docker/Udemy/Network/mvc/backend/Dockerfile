FROM node

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . .

EXPOSE 80

ENV MONGO_USER=root
ENV MONGO_PASS=secret

CMD ["npm", "start"]