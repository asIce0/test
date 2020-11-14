#!/usr/bin/env python

import socket

index = input('please input an port: ')

index = int(index)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex(('127.0.0.1', index))

if result == 0:
    print("Port %d is open" % index)
else:
    print("Port %d is not open" % index)

sock.close()

#注意：python3 里 input() 默认接收到的是 str 类型。将输入转换数值型