from flask import Flask

from config.settings import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route("/")
def main_page():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)