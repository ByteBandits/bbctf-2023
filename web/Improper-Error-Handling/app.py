from flask import Flask, request,render_template
import random
import string

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("/index.html")

import re

def generate_error_message(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

@app.route("/api/error")
def api_error():
    error_length = request.args.get("length", "")
    e = len(error_length)    
    if e == 32:
        return "Congratulations! You found the flag: BBCTF{tHis_i5_1t_Y0u_CraCk3D_iT}"
    elif e < 32:
        return "Error: Length too short"
    else:
        return generate_error_message(e)



if __name__ == "__main__":
    app.run(debug=True,port = 8000)
