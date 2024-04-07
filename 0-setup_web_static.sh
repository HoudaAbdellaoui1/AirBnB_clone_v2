#!/usr/bin/env bash
# Prepare web server
if ! command -v nginx &> /dev/null; then
    if [ -x "$(command -v apt-get)" ]; then
        apt-get update
        apt-get install nginx -y
    elif [ -x "$(command -v yum)" ]; then
        yum install epel-release -y
        yum install nginx -y
    else
        echo "Unsupported package manager, cannot install Nginx."
        exit 1
    fi
fi

chown -R $USER:$USER /data/web_static

mkdir -p /data/web_static/{releases/test,shared}

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

config_block="location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }"

sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
service nginx restart
