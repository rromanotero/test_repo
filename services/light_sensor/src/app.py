from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)

@app.route("/")
def salute():
    print("I'm light sensor v3 (stdout)")
    print("I'm light sensor v3 (stderr)", file=sys.stderr)
    return jsonify({
        "server_status" : 'OKKKAAAAAYYY (light sensor)'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
