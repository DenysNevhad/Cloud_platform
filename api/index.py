from flask import Flask, jsonify, request, send_file
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Шукаємо index.html
    html_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')
    if os.path.exists(html_path):
        return send_file(html_path)
    return jsonify({'message': 'Додайте index.html в корінь проекту'})

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

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        'status': 'success',
        'received_data': data,
        'timestamp': datetime.now().isoformat(),
        'method': 'POST'
    })

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({
            'error': 'Потрібні параметри a і b'
        }), 400
    
    try:
        a = float(data['a'])
        b = float(data['b'])
        
        return jsonify({
            'status': 'success',
            'input': {'a': a, 'b': b},
            'results': {
                'sum': a + b,
                'difference': a - b,
                'product': a * b,
                'division': a / b if b != 0 else 'infinity'
            },
            'timestamp': datetime.now().isoformat()
        })
    except (ValueError, TypeError):
        return jsonify({
            'error': 'Параметри мають бути числами'
        }), 400

if __name__ == '__main__':
    app.run()