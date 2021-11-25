from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return '<h1>{}</h1>'.format('はは')

app.run()