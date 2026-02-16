import os
from http.server import BaseHTTPRequestHandler, HTTPServer
# BaseHTTPRequestHandler: handles HTTP requests
# HTTPServer: creates an HTTP server to listen for requests

from dotenv import load_dotenv
# Import dotenv library to load environment variables from a .env file

load_dotenv()

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/value1":
             # This function is automatically called whenever the server receives a GET request
             # 'self' refers to the instance of MyHandler handling this specific request

            value = os.getenv("value1", "Environment variable not set")

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(value.encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyHandler)
     # Create an HTTP server instance with the specified address and request handler
    httpd.serve_forever()
     # Start the server and keep it running forever
     # This listens for incoming HTTP requests and dispatches them to MyHandler

#setx value1 "Hello from environment"
#to test:  python -c "import os; print(os.getenv('value1'))"
