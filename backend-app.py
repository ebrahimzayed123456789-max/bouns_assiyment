#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pod_name = os.environ.get('POD_NAME', 'unknown')
        namespace = os.environ.get('NAMESPACE', 'unknown')
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = f"<html><body><h1>Backend</h1><p>Pod: {pod_name}</p><p>Namespace: {namespace}</p></body></html>"
            self.wfile.write(response.encode())
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            r = f'{{"pod":"{pod_name}","namespace":"{namespace}","hostname":"{socket.gethostname()}"}}'
            self.wfile.write(r.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    print("Starting backend server on port 8080...")
    HTTPServer(('', 8080), SimpleHandler).serve_forever()
