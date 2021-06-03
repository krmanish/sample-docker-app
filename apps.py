import json

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello World'})


@app.route('/ack/<param>', methods=['GET'])
def ack(param):
    if not param or param.isdigit():
        return make_response(jsonify({"message": "Query Param must be a string"}), 404)

    return jsonify({'message': param.upper()})

@app.route('/postme', methods=['POST'])
def sample_post():

    if not request.is_json:
        return make_response(jsonify({"message": "Invalid Request"}), 404)

    data = json.loads(request.data, strict=False)
    if not data:
        return make_response(jsonify({"message": "No Payload"}), 404)

    if not data.get('foo'):
        return make_response(jsonify({"message": "'foo' key is missing"}), 404)

    data['message'] = 'Data parsed successfully'
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
