FROM alpine:3.11.5
RUN mkdir -p /app
COPY ./app /app
WORKDIR /app
