import chatbot
from flask import *

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def lnrs():
    if request.method == 'GET':
        return render_template('index.html', otp="")
    elif request.method == 'POST':
        query = request.form["query"]
        a=chatbot.querries(query)
        return render_template('index.html', otp=a)

if __name__ == '__main__':
    app.run(debug=True)