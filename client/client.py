#!/usr/bin/env python3
# Импортируем системную библиотеку python
# Она использует стя для загрузки файла 'index.html' с сервера
# Ничего устанавливать не надо, эта библиотека устанавливается вместе с python
import urllib.request
# Эта переменная содержит запрос к 'http://localhost:1234/'
fp = urllib.request.urlopen("http://localhost:1234/")
# 'encodedContent' соответствует закодированному ответу сервера ('index.html')
# 'decodedContent' соответствует раскодированному ответу сервера (то что будет выводиться на экран)
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")
# Выводми содержимое файла полученного с сервера ('index.html')
print(decodedContent)
# Закрываем соединение с сервером
fp.close()
