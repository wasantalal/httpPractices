from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the file to read from
FILE_PATH = "data.txt"  # Make sure this file exists in the same folder as this script

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/file":
            try:
                # Open and read the file
                with open(FILE_PATH, "r") as f:
                    content = f.read()

                # Send HTTP 200 OK
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()

                # Send the file content as the response
                self.wfile.write(content.encode())

            except FileNotFoundError:
                # If file does not exist, send 404
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"File not found")

        else:
            # For any other path, send 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")


if __name__ == "__main__":
    server_address = ("", 8000)  # Listen on all interfaces, port 8000
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on http://localhost:8000/file")
    httpd.serve_forever()
