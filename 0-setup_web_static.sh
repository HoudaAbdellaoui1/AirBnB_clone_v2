#!/usr/bin/env bash
# Prepare web server
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install nginx -y
fi

sudo chown -R $USER:$USER /data/web_static

sudo mkdir -p /data/web_static/{releases/test,shared}

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

config_block="location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }"

sudo sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
