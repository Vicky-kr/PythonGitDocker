from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello This is a python Docker Test"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
 