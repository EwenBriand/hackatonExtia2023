from flask import Flask, request, send_file, render_template
import python as back
from flask_cors import CORS
import sys
import asyncio
from waitress import serve

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def test():
    return back.test(), 200


@app.route('/get_CarBone', methods=['POST'])
def get_CarBone():
    data = None
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()

    if data is not None:
        res = back.get_car_transport(km=data['km'], type_v=data['type_v'])
        return str(res), 200
    else:
        return 'Bad request', 400


@app.route('/get_commonT_foot', methods=['POST'])
def get_commonT_foot():
    data = None
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()

    if data is not None:
        res = back.get_common_transport(
            km_bus=data["km_bus"], km_coach=data["km_coach"], km_rail=data["km_rail"], km_int_rail=data["km_int_rail"], km_tram=data["km_tram"], km_sub=data["km_sub"], km_taxi=data["km_taxi"])
        return str(res), 200
    else:
        return 'Bad request', 400


if __name__ == '__main__':
    # serve(app, host='0.0.0.0', port=8080)
    app.run(debug=True)

#  http://127.0.0.1:5000
