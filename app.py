from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return "<h1> Deployed to Heroku</h1>"


if __name__ == "__main__":
    app.run()