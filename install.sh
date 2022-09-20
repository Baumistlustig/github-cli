cp ./main.py ~/bin/github
touch ~/bin/data.env

pip install git github dotenv

echo "Successfully installed github-cli! Please paste ACCESS_TOKEN=<your access token> into ~/bin/data.env"