#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo 'testing' | sudo tee /data/web_static/releases/test/index.html
if [ -e /data/web_static/current ]; then
    sudo rm -F /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R 'ubuntu':'ubuntu' /data/
sudo rm /etc/nginx/sites-available/default
wget https://raw.githubusercontent.com/NamoDawn/AirBnB_clone_v2/master/default
sudo mv default /etc/nginx/sites-available/default
sudo service nginx restart
