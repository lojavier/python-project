#!/bin/sh
# https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04
# https://help.ubuntu.com/community/ApacheMySQLPHP
sudo apt-get -y update
sudo apt-get -y install apache2
sudo apt-get -y install mysql-client mysql-server php5-mysql
sudo mysql_install_db
sudo mysql_secure_installation
sudo apt-get -y install php5 libapache2-mod-php5 php5-mcrypt
# sudo nano /etc/apache2/mods-enabled/dir.conf
dir="
<IfModule mod_dir.c>
    DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm
</IfModule>
"
sudo printf %s "$dir" > /etc/apache2/mods-enabled/dir.conf
sudo service apache2 restart