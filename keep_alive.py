from flask import Flask
from threading import Thread

app = Flask('')
with open('index.html') as f:
  value = f.read()

@app.route('/')
def home():
    return value

def run():
    app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()