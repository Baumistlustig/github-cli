mkdir /usr/bin

cp ./main.py /usr/bin/github
touch /usr/bin/data.env

cd /usr/bin/

pip install gitpython pygithub python-dotenv

echo "Successfully installed github-cli! Please paste ACCESS_TOKEN=<your access token> into ~/bin/data.env"
