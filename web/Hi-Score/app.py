from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/", methods=["GET"])
def input():
    return render_template("index.html")


@app.route("/.secretion/flag", methods=["GET"])
def flag():
    return send_from_directory("static/.secretion", "flag")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
