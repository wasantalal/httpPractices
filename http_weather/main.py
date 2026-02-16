from http.server import BaseHTTPRequestHandler, HTTPServer
import requests  # For making HTTP requests to the weather API
import json

# Replace with your own OpenWeatherMap API key
API_KEY = "01923342c20844f0485ab05807a1ea90"

# API URL to get current weather for Amman, Jordan
WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q=Amman,JO&appid={API_KEY}&units=metric"
## Make request to OpenWeatherMap API for Amman, Jordan (parameters Amman, Jo and API key and metric units)

class WeatherHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/weather":
            try:
                # Call the external weather API
                response = requests.get(WEATHER_URL)
                data = response.json()  # Parse through JSON response

                # Extract relevant information
                weather_info = {
                    "city": data.get("name"),
                    "temperature": data.get("main", {}).get("temp"),
                    "description": data.get("weather", [{}])[0].get("description"),
                    "humidity": data.get("main", {}).get("humidity")
                }

                # Send HTTP response
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()

                # Send JSON data
                self.wfile.write(json.dumps(weather_info).encode())

            except Exception as e:
                # If something goes wrong, return an error
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error: {str(e)}".encode())

        else:
            # For any other path, return 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

if __name__ == "__main__":
    server_address = ("", 8000)  # Listen on all interfaces
    httpd = HTTPServer(server_address, WeatherHandler)
    print("Server running on http://localhost:8000/weather")
    httpd.serve_forever()
