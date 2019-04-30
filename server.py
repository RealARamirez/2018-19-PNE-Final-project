# Main server of my final project

# Import the libraries needed for the server
import http.server
import socketserver

# From the different files import the object and the functions needed
from Request import Request
from Client import Client, valid
from HTML_maker import HTMLFile
from JSON_maker import JSONFile

socketserver.TCPServer.allow_reuse_address = True

# Define the port
PORT = 8000

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            file = open("main.html", "r")
            content = file.read()
            file.close()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(content)))
            self.end_headers()
            self.wfile.write(str.encode(content))
        elif self.path == "/background_image.jpg":
            image = open("background_image.jpg", "rb")
            content = image.read()
            image.close()
            self.send_response(200)
            self.send_header('Content-Type', 'image/jpeg')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == "/favicon.ico":
            favicon = open("favicon.ico", "rb")
            content = favicon.read()
            favicon.close()
            self.send_response(200)
            self.send_header('Content-Type', 'image/x-icon')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        else:
            Req = Request(self.path)
            endpoint = Req.endpoint()
            parameters = Req.parameters()
            message = ""
            data = ""
            if Req.answer()["type"] == "client":
                data = Client(Req.answer()["value"])
                if valid(data)[0]: message, endpoint = valid(data)[1], "error"
            else: message, endpoint = Req.answer()["value"], "error"
            if Req.isjson():
                content = JSONFile(endpoint, message, data, parameters)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(str.encode(content)))
                self.end_headers()
                self.wfile.write(str.encode(content))
            else:
                content = HTMLFile(endpoint, message, data, parameters)
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(str.encode(content)))
                self.end_headers()
                self.wfile.write(str.encode(content))
        return

Handler = TestHandler



with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at Port: {}".format(PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Program stopped")
        httpd.server_close()

print("The server is stopped")