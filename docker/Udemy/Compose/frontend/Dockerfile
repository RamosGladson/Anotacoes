FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

#ENV PORTA=8001

CMD [ "npm", "start" ]