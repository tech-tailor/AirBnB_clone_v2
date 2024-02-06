#!/usr/bin/env bash
# set up web servers for deployment of webstatic

# Install Nginx if not already installed
apt-get update
apt-get -y install nginx


data_folder="/data/"
web_static_folder="$data_folder/web_static/"
releases_folder="$web_static_folder/releases/"
shared_folder="$web_static_folder/shared/"
test_folder="$releases_folder/test/"

mkdir -p "$data_folder" "$web_static_folder" "$releases_folder" "$shared_folder" "$test_folder"

# Create a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | tee "$test_folder/index.html" > /dev/null

ln -sfT "$test_folder"  "$web_static_folder/current"

chown -R ubuntu:ubuntu "$data_folder"

# Update Nginx configuration
nginx_config="/etc/nginx/sites-enabled/default"
nginx_alias="location /hbnb_static/ {\n\t\talias $web_static_folder/current/;\n\t}"

# Check if alias already exists in the Nginx configuration and remove it
sed -i '/location \/hbnb_static\//,/<\/location>/d' "$nginx_config"

# Add the new alias to the Nginx configuration
sed -i "s@^}\$@$nginx_alias\n\t}@" "$nginx_config"

# Restart Nginx
service nginx restart
