# -*- coding:utf-8 -*-
import socket, time, csv
ip_port = ('192.168.0.2', 8899) #连接对象OpenMV无线串口的IP和端口
sk = socket.socket()  #建立套接字对象
sk.connect(ip_port)   #建立连接
sk.settimeout(20)     #连接超时20秒

while True:
    data = sk.recv(1024)               #一次接收最大1024Byte数据
    try:
        ddata = eval(data.decode('utf-8')) #数据通过UTF-8转码后由String类型变为List类型
    except(TypeError):
        continue
    except(SyntaxError):
        continue
    except(UnicodeDecodeError):
        continue
        #尽管TCP提供了可靠的数据传输，但是由于无线传输的不稳定和设备自身等原因，还是会产生一些异常
        #以上排除了可能产生的三个异常：空数据、不完整的数据和编码错误的数据
    with open(r'data\zuobiao.csv', 'a', newline = '') as f: #将列表以追加形式写入csv文件
        wf = csv.writer(f)
        wf.writerow(ddata)
    print(ddata) #仅为笔记本查看数据需要
sk.close()