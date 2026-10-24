"""An API lets programs exchange data through a defined interface.
This example starts a small local HTTP endpoint and reads its JSON response.
"""

# Topic 33: Working with APIs
# This local example uses HTTP and JSON without needing an internet connection.

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from urllib.request import urlopen


class StudentAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/students":
            self.send_error(404, "Not found")
            return

        response = json.dumps(
            [{"name": "Maya", "score": 92}, {"name": "Leo", "score": 85}]
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format_string, *args):
        pass


def main():
    server = HTTPServer(("127.0.0.1", 0), StudentAPIHandler)
    server_thread = Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    try:
        url = f"http://127.0.0.1:{server.server_port}/students"
        with urlopen(url, timeout=5) as response:
            students = json.loads(response.read().decode("utf-8"))
        for student in students:
            print(f"{student['name']}: {student['score']}")
    finally:
        server.shutdown()
        server.server_close()
        server_thread.join()


if __name__ == "__main__":
    main()
