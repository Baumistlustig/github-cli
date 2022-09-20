#!/usr/bin/bash
mkdir /usr/bin

cp ./main.py /usr/bin/github
touch /usr/bin/.env

cd /usr/bin/ || exit

pip install gitpython pygithub python-dotenv

echo "Successfully installed github-cli!"

printf "Please enter your GitHub credentials "

read -p 'Username: ' username
read -sp 'Access Token: ' access_token

echo
echo "USERNAME=$username" > .env
echo "\n" > data.env
echo "ACCESS_TOKEN=$access_token" >> .env
