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

if __name__ == '__main__':
    # serve(app, host='0.0.0.0', port=8080)
    app.run(debug=True)

#  http://127.0.0.1:5000
