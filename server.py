from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
import webbrowser

class ClockServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('clock.html', 'rb') as file:
            self.wfile.write(file.read())

def run_server(server_class=HTTPServer, handler_class=ClockServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port %d...' % port)
    webbrowser.open('http://localhost:8000')
    httpd.serve_forever()

run_server()
