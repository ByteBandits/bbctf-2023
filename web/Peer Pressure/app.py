from flask import Flask, render_template, request, redirect, Response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "HEAD"])
def input():
    return render_template("index.html", result="")


@app.route("/aGVhZA==", methods=["GET", "POST", "HEAD"])
def rickroll():
    if request.method == "GET":
        return redirect("https://youtu.be/dQw4w9WgXcQ")

    if request.method == "HEAD":
        resp = Response("lol rick")
        resp.headers[
            "link"
        ] = "magnet:?xt=urn:btih:CE7CE0D5E1E72943485F26EC624AF55CE0C3B3F2&dn=flag.txt&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce"
        return resp

    return render_template("index.html", result="")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
