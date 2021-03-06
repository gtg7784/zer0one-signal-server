from flask import Flask, jsonify, request
from serial import Serial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='127.0.0.1', help='host')
parser.add_argument('--serial', type=str, default='/dev/ttyACM0', help='port')
args = parser.parse_args()

ser = Serial(args.serial, 9600)
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'})

@app.route('/detected', methods=['POST'])
def detected():
    index = request.json['index']
    ser.write(f'{index}'.encode('utf-8'))
    return jsonify({'message': 'Detected!'})

if __name__=="__main__":
    app.run(host=args.host, port="80", debug=True)
