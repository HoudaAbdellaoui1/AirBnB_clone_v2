#!/usr/bin/env bash
# Prepare web server
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared

mkdir -p /data/web_static/{releases/test,shared}

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

chown -R $USER:$USER /data/web_static

config_block="location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }"

sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
service nginx start
