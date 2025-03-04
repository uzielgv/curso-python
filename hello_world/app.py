from flask import Flask

app = Flask(__name__)

@app.route("/") # Home or root of website
def index():
    return '<html><head><title>HELLO WORLD</title></head><body><h1>Hello world</h1><p>Ir a <a href="/about">about</a></p></body></html>'

@app.route("/about") # Info about this site
def about():
    return '<html><head><title>About this page</title></head><body>Everything about this website. Back to <a href="/">Hello world</a></body></html>'

if __name__ == "__main__":
    app.run(debug=True)