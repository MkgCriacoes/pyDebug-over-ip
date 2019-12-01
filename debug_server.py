from flask import Flask, request

app = Flask(__name__, static_folder="site")

import logging
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

@app.route("/")
def msg():
    print("Debug: " + request.args.get("msg"))
    return "Ok"

if __name__ == "__main__":
    ip = "0.0.0.0"
    app.run(host=ip, port=8080, debug=True)