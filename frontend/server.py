from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

if __name__ == "__main__":
    port = 8080
    print(f"Serving frontend at http://127.0.0.1:{port}")
    httpd = HTTPServer(('127.0.0.1', port), CORSRequestHandler)
    httpd.serve_forever() 