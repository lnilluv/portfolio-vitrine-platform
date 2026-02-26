import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from portfolio_api.composition_root.bootstrap import build_list_projects_use_case


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/healthz":
            self._write_json(200, {"status": "ok"})
            return

        if self.path == "/projects":
            use_case = build_list_projects_use_case()
            self._write_json(200, use_case.execute())
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


def run() -> None:
    server = HTTPServer(("0.0.0.0", 8000), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    run()
