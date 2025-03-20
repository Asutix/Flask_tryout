from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello world!</p>"

#git checkout -b main
#response: Switched to a new branch 'main'
#wat betekent dit? > Dat je een nieuwe branch hebt aangemaakt die "main" heet en dat je hier naar veranderd bent