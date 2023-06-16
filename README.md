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
```
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