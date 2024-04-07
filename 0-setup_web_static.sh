#!/usr/bin/env bash
# Prepare web server
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

sudo mkdir -p /data/web_static/{releases/test,shared}

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R $USER:$USER /data/web_static

config_block="location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }"

sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
service nginx start
