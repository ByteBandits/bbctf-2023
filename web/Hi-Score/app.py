import http.server
import socketserver

PORT = 8080

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
