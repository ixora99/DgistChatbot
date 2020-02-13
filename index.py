# -*- coding: utf-8 -*-i

import os
from flask import Flask, request, jsonify
import opentimemodule

app = Flask(__name__)

@app.route('/opentime',methods=['POST'])
def test():
    dataReceive = request.get_json()
    opendate = opentimemodule.check()
    dataSend = {
            "type" : opendate
            }

    return jsonify(dataSend)

@app.route('/middledday',methods=['POST'])
def test2():
    dataReceive = request.get_json()
    middledday=opentimemodule.middledday()

    dataSend = {
            "data" : middledday
            }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
