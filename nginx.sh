#!/bin/bash

sudo cp -rf m.conf /etc/nginx/sites-available/m
chmod 710 /var/lib/jenkins/workspace/adhikar

sudo ln -s /etc/nginx/sites-available/m /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx
