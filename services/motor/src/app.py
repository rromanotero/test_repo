from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def salute():
    print("I'm motor v2")
    return jsonify({
        "server_status" : 'OKKKAAAAAYYY (motor)'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
