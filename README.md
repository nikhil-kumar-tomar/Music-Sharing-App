# Usage
This web app allows logged in users to upload music and share it with others, There are 3 sharing methods available on this platform listed below:
Music Type  | Description
------------- | -------------
Public  | Uploaded music is available to all the users on the platform
Private  | Uploaded music is not available to anyone except the owner.
Protected  | Uploaded music is available only to the registered users whose emails were provided by the owner at the time of upload.

**Owner** is the user who uploaded the music. 

# Deployment
1. move the .env with configured details to Music-Sharing-App/music_app/music_app/ </br>
2. In current folder create a .venv folder and initialize a virtual env
3. In you virtual env run commmand `pip install -r music_app/requirements.txt` To install all the necessary dependencies </br>
4.  launch your process by using command `gunicorn -c config_gunicorn/gunicorn_config.py music_app.wsgi`

contents of gunicorn_config.py
```python
command='/home/ubuntu/Music-Sharing-App/.venv/bin/gunicorn'
pythonpath='/home/ubuntu/Music-Sharing-App/music_app'
bind='127.0.0.1:8000'
workers=3
timeout=90
```
</br>
5.  Finally configure nginx with default configuration file

contents of nginx default file 
</br>
```python
server {
        listen 80;
        server_name <IP Address of your machine>;


location /static/ {
        alias /home/ubuntu/Music-Sharing-App/music_app/static/;
}

location /media/ {
        alias /home/ubuntu/Music-Sharing-App/music_app/media/;
}

location / {
        proxy_pass http://127.0.0.1:8000;
        }
}
```
6. Make sure folders `static` and `media` are given access to nginx, use nginx.conf to see the user value and change these folder permissions for that user  
7. Finally run command `sudo systemctl restart nginx`

