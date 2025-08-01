#!/usr/bin/env python3
import http.server
import socketserver
import json

PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server running on http://localhost:{PORT}")
        httpd.serve_forever()