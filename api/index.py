from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Demo - Лабораторна робота</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .card h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.5em;
        }
        
        .input-group {
            margin-bottom: 15px;
        }
        
        .input-group label {
            display: block;
            margin-bottom: 5px;
            color: #333;
            font-weight: 600;
        }
        
        .input-group input, .input-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        .input-group input:focus, .input-group textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
            width: 100%;
        }
        
        button:hover {
            transform: translateY(-2px);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        .response {
            margin-top: 20px;
            padding: 15px;
            background: #f5f5f5;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            display: none;
        }
        
        .response.show {
            display: block;
        }
        
        .response pre {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-size: 14px;
        }
        
        .status-badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .status-success {
            background: #4caf50;
            color: white;
        }
        
        .status-error {
            background: #f44336;
            color: white;
        }
        
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        
        @media (max-width: 600px) {
            .grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 API Demo</h1>
            <p>Лабораторна робота - Deployment на Vercel</p>
        </div>
        
        <div class="card">
            <h2>📨 Post</h2>
            <p style="margin-bottom: 20px; color: #666;">Надішли JSON і отримай його назад</p>
            
            <div class="input-group">
                <label for="echoName">Ім'я:</label>
                <input type="text" id="echoName" placeholder="Введіть ім'я">
            </div>
            
            <div class="input-group">
                <label for="echoMessage">Повідомлення:</label>
                <textarea id="echoMessage" rows="3" placeholder="Введіть повідомлення"></textarea>
            </div>
            
            <button onclick="sendEcho()">Надіслати</button>
            
            <div id="echoResponse" class="response"></div>
        </div>
        
        <div class="card">
            <h2>🧮 Калькулятор</h2>
            <p style="margin-bottom: 20px; color: #666;">Виконай математичні операції</p>
            
            <div class="grid">
                <div class="input-group">
                    <label for="numA">Число A:</label>
                    <input type="number" id="numA" placeholder="0" value="10">
                </div>
                
                <div class="input-group">
                    <label for="numB">Число B:</label>
                    <input type="number" id="numB" placeholder="0" value="5">
                </div>
            </div>
            
            <button onclick="calculate()">Обчислити</button>
            
            <div id="calcResponse" class="response"></div>
        </div>
        
        <div class="card">
            <h2>✅ GET Request</h2>
            <p style="margin-bottom: 20px; color: #666;">Перевір основний endpoint</p>
            
            <button onclick="testGet()">Тестувати GET /api/test</button>
            
            <div id="getResponse" class="response"></div>
        </div>
    </div>
    
    <script>
        async function sendEcho() {
            const name = document.getElementById('echoName').value;
            const message = document.getElementById('echoMessage').value;
            const responseDiv = document.getElementById('echoResponse');
            
            try {
                const response = await fetch('/api/echo', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, message })
                });
                
                const data = await response.json();
                
                responseDiv.innerHTML = `
                    <span class="status-badge status-success">Success</span>
                    <pre>${JSON.stringify(data, null, 2)}</pre>
                `;
                responseDiv.classList.add('show');
            } catch (error) {
                responseDiv.innerHTML = `
                    <span class="status-badge status-error">Error</span>
                    <pre>${error.message}</pre>
                `;
                responseDiv.classList.add('show');
            }
        }
        
        async function calculate() {
            const a = parseFloat(document.getElementById('numA').value);
            const b = parseFloat(document.getElementById('numB').value);
            const responseDiv = document.getElementById('calcResponse');
            
            try {
                const response = await fetch('/api/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ a, b })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    responseDiv.innerHTML = `
                        <span class="status-badge status-success">Success</span>
                        <pre>${JSON.stringify(data, null, 2)}</pre>
                    `;
                } else {
                    responseDiv.innerHTML = `
                        <span class="status-badge status-error">Error</span>
                        <pre>${JSON.stringify(data, null, 2)}</pre>
                    `;
                }
                responseDiv.classList.add('show');
            } catch (error) {
                responseDiv.innerHTML = `
                    <span class="status-badge status-error">Error</span>
                    <pre>${error.message}</pre>
                `;
                responseDiv.classList.add('show');
            }
        }
        
        async function testGet() {
            const responseDiv = document.getElementById('getResponse');
            
            try {
                const response = await fetch('/api/test');
                const data = await response.json();
                
                responseDiv.innerHTML = `
                    <span class="status-badge status-success">Success</span>
                    <pre>${JSON.stringify(data, null, 2)}</pre>
                `;
                responseDiv.classList.add('show');
            } catch (error) {
                responseDiv.innerHTML = `
                    <span class="status-badge status-error">Error</span>
                    <pre>${error.message}</pre>
                `;
                responseDiv.classList.add('show');
            }
        }
    </script>
</body>
</html>
    '''

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