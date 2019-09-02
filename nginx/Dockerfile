FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY ../youtube/static /static
COPY ../youtube/media /media

#RUN mkdir -p /var/www/media
#RUN mkdir -p /var/www/static

#WORKDIR /media
#RUN chown -R nginx:nginx /var/www/media

#WORKDIR /static
#RUN chown -R nginx:nginx /var/www/static
