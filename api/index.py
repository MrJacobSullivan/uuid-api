from http.server import BaseHTTPRequestHandler
from urllib import parse
from uuid import uuid4


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        response = str(uuid4())
        self.wfile.write(response.encode())
        return
