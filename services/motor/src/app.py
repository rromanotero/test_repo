from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)

@app.route("/")
def salute():
    print("I'm motor v3 (stdout)")
    print("I'm motor v3 (stderr)", file=sys.stderr)
    return jsonify({
        "server_status" : 'OKKKAAAAAYYY (motor)'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
