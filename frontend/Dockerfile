FROM node:16-alpine

WORKDIR /usr/src/app

# add path
ENV PATH /usr/src/app/node_modules.bin:$PATH

# install and cache app dependencies
COPY app/package.json .
COPY app/package-lock.json .

# npm install
RUN npm ci
RUN npm install react-scripts@5.0.1 -g --silent

CMD [ "npm", "start" ]
