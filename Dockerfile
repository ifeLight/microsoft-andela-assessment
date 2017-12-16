# create a file named Dockerfile, then Using The lightweight Alpine Image
#FROM alpine:3.1

FROM node:latest

# Update
#RUN apk add --update nodejs

# Update npm to latest
#RUN npm install npm@latest -g

#Update node to the most stable version
#CMD ["npm", "cache", "clean", "-f"]
#CMD ["npm",  "install", "-g ", "n"]
#CMD ["n",  "stable"]


RUN mkdir /app
WORKDIR /app

COPY package.json /app
CMD ["npm",  "install"]

COPY . /app

EXPOSE 8000

CMD ["node", "--version"]

CMD ["npm", "start"]