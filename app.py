from flask import Flask

app = Flask(__name)__

@app.route('/')

def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
