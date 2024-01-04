git pull
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations --merge --noinput
python3 manage.py migrate
python3 manage.py collectstatic --noinput
deactivate
sudo systemctl restart mountblue
sudo systemctl restart nginx
echo "DONE! :)"