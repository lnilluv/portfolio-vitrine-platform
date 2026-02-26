import json
from http.server import BaseHTTPRequestHandler, HTTPServer

def create_handler(list_projects_use_case):
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            if self.path == "/healthz":
                self._write_json(200, {"status": "ok"})
                return

            if self.path == "/projects":
                self._write_json(200, list_projects_use_case.execute())
                return

            self._write_json(404, {"error": "not found"})

        def log_message(self, format: str, *args: object) -> None:  # noqa: A003
            return

        def _write_json(self, status_code: int, payload: object) -> None:
            body = json.dumps(payload).encode("utf-8")
            self.send_response(status_code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    return RequestHandler


def run(list_projects_use_case) -> None:
    server = HTTPServer(("0.0.0.0", 8000), create_handler(list_projects_use_case))
    server.serve_forever()
