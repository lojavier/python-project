#!/bin/bash

# https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04
# https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04
# https://help.ubuntu.com/community/ApacheMySQLPHP

ip_address=""
APACHE=FALSE
APACHE_FULL=FALSE
APACHE_SECURE=FALSE

function get_ip_address()
{
	ip_address=`ip addr show eth1 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//' | sed -rn '/((1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])/p'`
	# ip_address=`curl http://icanhazip.com`
	return 0
}

#----------------------------------------------------------------
# LINUX
#----------------------------------------------------------------
sudo -S apt-get -y update

#----------------------------------------------------------------
# APACHE
#----------------------------------------------------------------
sudo -S apt-get -y install apache2
get_ip_address
sudo -S grep -e 'ServerName' /etc/apache2/apache2.conf >/dev/null
if [ $? -ne 0 ]; then
	sudo -S sh -c "printf '\nServerName %s\n' '$ip_address' >> /etc/apache2/apache2.conf"
else
	ServerNameIP=`grep -e 'ServerName' /etc/apache2/apache2.conf | awk '{ print $2; }'`
	if [[ -z "$ServerNameIP" ]] || [[ "$ip_address" != "$ServerNameIP" ]]; then
		sudo -S sed -i "s/ServerName.*/ServerName ${ip_address}/" /etc/apache2/apache2.conf
	fi
fi
echo "ServerName $ip_address"
configtest="$(sudo -S apache2ctl configtest 2>&1 >/dev/null)"
if [[ "$configtest" == *"AH00558"* ]]; then
	echo "$configtest"
	echo "ERROR: Failed to update /etc/apache2/apache2.conf with fully qualified domain name/ip"
	exit 1
fi
sudo -S service apache2 restart
temp=`sudo -S ufw app list | sed 's/^[ \t]*//;s/[ \t]*$//'`
IFS=$'\n' read -rd '' -a ufw_app_list <<< "$temp"
for element in "${ufw_app_list[@]}"; do
	case "$element" in
		"Apache")
			APACHE=TRUE
			;;
		"Apache Full")
			APACHE_FULL=TRUE
			;;
		"Apache Secure")
			APACHE_SECURE=TRUE
			;;
		*)
			;;
	esac
done
if [[ "$APACHE" == "FALSE" ]] || [[ "$APACHE_FULL" == "FALSE" ]] || [[ "$APACHE_SECURE" == "FALSE" ]]; then
	if [ "$APACHE" == "FALSE" ]; then
		echo "ERROR: Missing Apache app"
	fi
	if [ "$APACHE_FULL" == "FALSE" ]; then
		echo "ERROR: Missing Apache Full app"
	fi
	if [ "$APACHE_SECURE" == "FALSE" ]; then
		echo "ERROR: Missing Apache Secure app"
	fi
	exit 1
fi
sudo -S ufw allow in "Apache Full"

#----------------------------------------------------------------
# MYSQL
#----------------------------------------------------------------
sudo -S apt-get -y install mysql-server
sudo -S apt-get -y install mysql-client
sudo -S mysql_install_db
sudo -S mysql_secure_installation

#----------------------------------------------------------------
# PHP
#----------------------------------------------------------------
sudo -S apt-get -y install php5 libapache2-mod-php5 php5-mcrypt php5-mysql
sudo -S grep -e 'DirectoryIndex index.php' /etc/apache2/mods-enabled/dir.conf >/dev/null
if [ $? -ne 0 ]; then
	sudo -S sed -i "s/.*DirectoryIndex.*/\tDirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm/" /etc/apache2/mods-enabled/dir.conf
fi

sudo -S service apache2 restart
sudo -S service apache2 status

#----------------------------------------------------------------
# EXTRA
#----------------------------------------------------------------
# apt-cache search php5-
# sudo -S apt-get -y install php5-json
# sudo -S apt-get -y install curl
