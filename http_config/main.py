from http.server import BaseHTTPRequestHandler, HTTPServer
import configparser
import json  # To send JSON responses

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")  # Make sure config.ini is in the same folder

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/value1":
            # Read the value from the [settings] section
            value = config.get("settings", "value1", fallback=None)

            if value is None:
                # If the value is missing, send 404
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Value not found"}).encode())
                return
            #json.dumps() converts a Python object into a JSON-formatted string.
            #encode() converts the string into bytes using UTF-8 encoding
            #self.wfile.write(...) sends the JSON response to whoever made the GET request.

            # Build a JSON response
            response_data = {"value1": value}

            # Send HTTP 200 OK with JSON content type
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # Send JSON response
            self.wfile.write(json.dumps(response_data).encode())

        else:
            # For any other path, return 404
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())


if __name__ == "__main__":
    server_address = ("", 8000) 
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on http://localhost:8000/value1")
    httpd.serve_forever()
