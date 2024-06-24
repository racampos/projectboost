import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

PORT = 8000
handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()

