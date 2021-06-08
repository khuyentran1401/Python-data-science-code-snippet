# Generate config

jupyter notebook --generate-config
# Allow remote access

echo "c.NotebookApp.allow_remote_access = True" >> ~/.jupyter/jupyter_notebook_config.py

jupyter notebook

ngrok http 8888
