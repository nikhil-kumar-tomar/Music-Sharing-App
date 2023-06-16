# Example config, replace ubuntu or path according to your need 
command='/home/ubuntu/Music-Sharing-App/.venv/bin/gunicorn'
pythonpath='/home/ubuntu/Music-Sharing-App/music_app'
bind='127.0.0.1:8000'
workers=3
timeout=90