# Stubs for werkzeug.serving (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from socketserver import ThreadingMixIn, ForkingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler

class _SslDummy:
    def __getattr__(self, name): ...

ssl = ...  # type: Any
LISTEN_QUEUE = ...  # type: Any
can_open_by_fd = ...  # type: Any

class WSGIRequestHandler(BaseHTTPRequestHandler):
    @property
    def server_version(self): ...
    def make_environ(self): ...
    environ = ...  # type: Any
    close_connection = ...  # type: Any
    def run_wsgi(self): ...
    def handle(self): ...
    def initiate_shutdown(self): ...
    def connection_dropped(self, error, environ=None): ...
    raw_requestline = ...  # type: Any
    def handle_one_request(self): ...
    def send_response(self, code, message=None): ...
    def version_string(self): ...
    def address_string(self): ...
    def port_integer(self): ...
    def log_request(self, code='', size=''): ...
    def log_error(self, *args): ...
    def log_message(self, format, *args): ...
    def log(self, type, message, *args): ...

BaseRequestHandler = ...  # type: Any

def generate_adhoc_ssl_pair(cn=None): ...
def make_ssl_devcert(base_path, host=None, cn=None): ...
def generate_adhoc_ssl_context(): ...
def load_ssl_context(cert_file, pkey_file=None, protocol=None): ...

class _SSLContext:
    def __init__(self, protocol): ...
    def load_cert_chain(self, certfile, keyfile=None, password=None): ...
    def wrap_socket(self, sock, **kwargs): ...

def is_ssl_error(error=None): ...
def select_ip_version(host, port): ...

class BaseWSGIServer(HTTPServer):
    multithread = ...  # type: Any
    multiprocess = ...  # type: Any
    request_queue_size = ...  # type: Any
    address_family = ...  # type: Any
    app = ...  # type: Any
    passthrough_errors = ...  # type: Any
    shutdown_signal = ...  # type: Any
    host = ...  # type: Any
    port = ...  # type: Any
    socket = ...  # type: Any
    server_address = ...  # type: Any
    ssl_context = ...  # type: Any
    def __init__(self, host, port, app, handler=None, passthrough_errors=False, ssl_context=None, fd=None): ...
    def log(self, type, message, *args): ...
    def serve_forever(self): ...
    def handle_error(self, request, client_address): ...
    def get_request(self): ...

class ThreadedWSGIServer(ThreadingMixIn, BaseWSGIServer):
    multithread = ...  # type: Any
    daemon_threads = ...  # type: Any

class ForkingWSGIServer(ForkingMixIn, BaseWSGIServer):
    multiprocess = ...  # type: Any
    max_children = ...  # type: Any
    def __init__(self, host, port, app, processes=40, handler=None, passthrough_errors=False, ssl_context=None, fd=None): ...

def make_server(host=None, port=None, app=None, threaded=False, processes=1, request_handler=None, passthrough_errors=False, ssl_context=None, fd=None): ...
def is_running_from_reloader(): ...
def run_simple(hostname, port, application, use_reloader=False, use_debugger=False, use_evalex=True, extra_files=None, reloader_interval=1, reloader_type='', threaded=False, processes=1, request_handler=None, static_files=None, passthrough_errors=False, ssl_context=None): ...
def run_with_reloader(*args, **kwargs): ...
def main(): ...
