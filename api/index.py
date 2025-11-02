from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/api')
def hello():
    return jsonify({
        'message': 'API працює!',
        'timestamp': datetime.now().isoformat(),
        'method': request.method
    })

@app.route('/api/test')
def test():
    return jsonify({
        'status': 'success',
        'data': 'Тестовий endpoint працює',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run()