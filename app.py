from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello PrepTrack!"

if __name__ == "__main__":
    app.run(debug=True)
