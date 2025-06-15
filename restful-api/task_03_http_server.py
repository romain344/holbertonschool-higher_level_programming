#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_json({"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/status":
            self._send_json({"status": "OK"})
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

def run():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()