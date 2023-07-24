FROM alpine
RUN apk add --update nodejs npm
RUN npm install -g http-server
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD ["http-server", "-p", "8080"]