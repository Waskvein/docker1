#! /usr/bin/#!/usr/bin/env python3
# Импорт системных библиотек python
# Эти библиотеки будут использоваться для создания веб сервера.
import http.server
import socketserver
# переменная для обработки запросов от клиента к серверу
handler = http.server.SimpleHTTPRequestHandler
# Тут мы указываем, что сервер мы хотим запустить на порте 1234
with socketserver.TCPServer(("",1234),handler) as httpd:
    # благодаря этой команде сервер будет выполняться постоянно, ожидая запросов от клиентов
    httpd.serve_forever()
