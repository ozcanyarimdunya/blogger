FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY docker/nginx/default.conf /etc/nginx/conf.d

RUN mkdir -p /app/media-files/
RUN chmod 777 /app/media-files/
