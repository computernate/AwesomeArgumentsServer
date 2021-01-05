# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:11:55 2021

@author: u1095732
"""

import socket

print("Requesting")
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8080))
serv.listen(5)
counter = 0
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode("utf-8")
        print(from_client)
        toSend = b'HTTP/1.0 200 OK\nContent-'
        toSend2= b'Type: text/html; charset=UTF-8\n\n<html><head></head><body><p>Hello</p></body></html>\r\n\r\n'
        
        conn.sendall(toSend)
        conn.sendall(toSend2)
        
    conn.close()
    print('client disconnected')
    
    

