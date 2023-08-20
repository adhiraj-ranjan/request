import subprocess

with open('~/.streamlit/credentials.toml') as f:
  f.write('email = ""')

subprocess.Popen("streamlit run main.py --server.address 0.0.0.0 --server.port 8080", shell=True)