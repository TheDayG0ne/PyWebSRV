# -*- coding: cp1251 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer

html = "<html><body>Привет! Это тестовая страница данного веб-сервера. Изменить код сайта можно в файле webserver.py   Больше информации на GitHub: https://github.com/TheDayG0ne/PyWebSRV</body></html>"

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))

def server_thread(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    port = 8000
    print("Starting server at port %d" % port)
    server_thread(port)
