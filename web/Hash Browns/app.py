from flask import Flask, render_template, request,redirect
from flask import make_response

app = Flask(__name__)

@app.route("/", methods=['GET','POST','HEAD'])
def input():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('garlic', "cmztpaurxxnoqz3p2on73msbohg5sk74l2fxnxp27gky6cdjqzqq6nad")
    return resp

if __name__ == "__main__":
     app.run(debug=True,port=8000)
