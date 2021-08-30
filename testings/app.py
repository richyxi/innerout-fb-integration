import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")

facebook_bp = make_facebook_blueprint(
    client_id="",
    client_secret="",
)
app.register_blueprint(facebook_bp, url_prefix="/login")

@app.route("/")
def index():
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))
    resp = facebook.get("/me?fields=name,email,picture")
    #assert resp.ok
    print(resp.json())
    return "bellaquera me twitteo aunque no me menciono"
    #return "You are @{login} on facebook".format(login=resp.json()["login"])

if __name__ == "__main__":
    app.run(host="localhost", ssl_context='adhoc')
