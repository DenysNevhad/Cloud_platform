from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Парсимо URL
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query = urllib.parse.parse_qs(parsed_path.query)
        
        timestamp = datetime.now().isoformat()
        
        # Роутинг
        if path == '/api' or path == '/api/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'message': 'Hello from Python on Vercel!',
                'timestamp': timestamp,
                'method': 'GET',
                'deployed': True
            }
            self.wfile.write(json.dumps(response).encode())
            return
        
        if path == '/api/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'status': 'OK',
                'timestamp': timestamp,
                'language': 'Python 3.9'
            }
            self.wfile.write(json.dumps(response).encode())
            return
        
        if path.startswith('/api/echo'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'message': 'Echo endpoint',
                'query_params': query,
                'timestamp': timestamp
            }
            self.wfile.write(json.dumps(response).encode())
            return
        
        # 404
        self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'error': 'Not Found',
            'availableEndpoints': ['/api', '/api/health', '/api/echo']
        }
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        
        try:
            data = json.loads(body) if body else {}
        except:
            data = {}
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'message': 'POST request received',
            'data': data,
            'timestamp': datetime.now().isoformat()
        }
        self.wfile.write(json.dumps(response).encode())