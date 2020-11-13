from http.server import BaseHTTPRequestHandler, HTTPServer

html = '<html><body><h3>Hello from the Raspberry Pi</h3><img src="650.png"/></body></html>'

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
    
    def do_GET(self):
        print("GET request, Path:", self.path)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        elif self.path.endswith(".png"):
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            with open(os.curdir + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))


if __name__ == '__main__':
    port = 8000
    print("Starting server at port %d" % port)
    server_thread(port)


