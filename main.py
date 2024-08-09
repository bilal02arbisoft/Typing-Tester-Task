import socket
from io import BytesIO
from wsgi import typing_tester

class WSGIServer:

    def __init__(self, app, host, port):

        self.headers = None
        self.status = None
        self.app = app
        self.host = host
        self.port = port

    def serve_forever(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Serving on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            self.handle_request(client_socket)
            client_socket.close()

    def handle_request(self, client_socket):
        request_data = client_socket.recv(1024).decode("utf-8")
        print(f'Request received: {request_data}')
        environ = self.parse_request(request_data)
        response_body = self.app(environ, self.start_response)
        response = self.build_response(response_body)
        client_socket.sendall(response)

    def parse_request(self, request_data):
        lines = request_data.splitlines()
        request_line = lines[0].split()
        if len(request_line) == 3:

            method, path, version = request_line
        else:
            method = path = version = None

        environ = {
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
            'SERVER_PROTOCOL': version,
        }

        headers = {}

        header_lines = lines[1:]
        for line in header_lines:
            if not line.strip():

                break
            if ': ' in line:

                header, value = line.split(': ', 1)
                headers[header.upper()] = value

        for header, value in headers.items():
            environ['HTTP_' + header] = value

        if 'CONTENT-LENGTH' in headers:

            try:
                content_length = int(headers['CONTENT-LENGTH'])
            except ValueError:
                content_length = 0
            environ['CONTENT_LENGTH'] = content_length

            body_start_index = len(request_data) - content_length
            environ['wsgi.input'] = BytesIO(request_data[body_start_index:].encode('utf-8'))

        content_type = headers.get('CONTENT-TYPE', '').lower()

        if content_type == 'application/json':

            environ['CONTENT_TYPE'] = 'json'
        elif content_type == 'text/plain':

            environ['CONTENT_TYPE'] = 'text'
        else:
            environ['CONTENT_TYPE'] = 'unknown'

        return environ

    def start_response(self, status, headers):
        self.status = status
        self.headers = headers

    def build_response(self, response_body):
        response = f'HTTP/1.1 {self.status}\n'
        for header in self.headers:
            response += f'{header[0]}: {header[1]}\r\n'

        response += '\r\n'
        if isinstance(response_body, list):

            response_body = [part.encode('utf-8') if isinstance(part, str) else part for part in response_body]

        response = response.encode('utf-8')+b''.join(response_body)

        return response


if __name__ == '__main__':

    server = WSGIServer(host='localhost', port=8000, app=typing_tester)
    server.serve_forever()








