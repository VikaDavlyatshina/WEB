# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

# Настройки запуска
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """ Обрабатывает GET-запросы """
        # Если запрашивается CSS файл
        if self.path.endswith('.css'):
            self.serve_file('styles.css', 'text/css')
        # Все остальные запросы → контакты
        else:
            self.serve_file('contacts.html', 'text/html')

    def serve_file(self, filename, content_type):
        """ Отдает файл """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()

            self.send_response(200)
            self.send_header('Content-type', f'{content_type}; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))

        except FileNotFoundError:
            self.send_error(404, f"File {filename} not found")


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")