from flask import Flask, jsonify, request
from serial import Serial

ser = Serial('/dev/ttyACM0', 9600)
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'})

@app.route('/detected', method=['POST'])
def detected():
    index = request.json['index']
    ser.write(f'{index}'.encode('utf-8'))
    return jsonify({'message': 'Detected!'})

if __name__=="__main__":
  app.run(host="0.0.0.0", port="80", debug=True)