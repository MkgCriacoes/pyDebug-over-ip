from flask import Flask, request

app = Flask(__name__, static_folder="site")

import logging
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

logs = ""

@app.route("/sendlog")
def msg():
    global logs
    print("Debug: " + request.args.get("msg"))

    logs = "Debug: " + request.args.get("msg") + "<br>" + logs
    return "Ok"

@app.route("/")
def home():
    global logs
    return """<script>
                setTimeout(function(){
                    location.reload();
                }, 500)
              </script>
              <h3>""" + logs + """</h3>"""

if __name__ == "__main__":
    ip = "0.0.0.0"
    app.run(host=ip, port=8080, debug=True)