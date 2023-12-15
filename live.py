import http.server
import socketserver

PORT = 5500  # Escolha uma porta disponível

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    httpd.serve_forever()
