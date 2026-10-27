
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>RedKross Web Security Lab</h1><p>Your local web application is running.</p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)





from app import app


def test_home_page_returns_success():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"RedKross Web Security Lab" in response.data
