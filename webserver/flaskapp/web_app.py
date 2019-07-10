from flask import Flask
app = Flask(__name__)

@app.route('/')
def start_app():
    return 'Flask app running.'

if __name__ == "__main__":
    app.run(host='0.0.0.0')