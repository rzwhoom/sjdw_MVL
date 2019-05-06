# -*- coding:utf-8 -*-
import tkinter as tk
import socket

zt = ('SimHei', 12)

ip_port = ('192.168.0.3', 8899)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

def zpz():
    sk.send('e'.encode('utf-8'))
    #pass
def qj():
    sk.send('a'.encode('utf-8'))
    #pass
def ypz():
    sk.send('f'.encode('utf-8'))
    #pass
def zjz():
    sk.send('d'.encode('utf-8'))
    #pass
def yjz():
    sk.send('c'.encode('utf-8'))
    #pass
def tz():
    sk.send('b'.encode('utf-8'))
    #pass
def tc():
    sk.send('b'.encode('utf-8'))
    sk.close()
    root.quit()
    root.destroy()
    #pass

root = tk.Tk()
root.wm_title('视觉定位之小车遥控程序')
root.iconbitmap('tb.ico')
root.geometry('204x180+700+0')
root.resizable(width = False, height = False)

label = tk.Label(master = root, text = '视觉定位之小车遥控程序', font = zt) 
label.grid(row = 0, column = 0, pady = 20, padx = 10, columnspan = 3)
button1 = tk.Button(master = root, text = '左偏转', command = zpz) 
button1.grid(row = 1, column = 0) 
button2 = tk.Button(master = root, text = '前  进', command = qj)
button2.grid(row = 1, column = 1) 
button3 = tk.Button(master = root, text = '右偏转', command = ypz)
button3.grid(row = 1, column = 2) 
button4 = tk.Button(master = root, text = '左急转', command = zjz) 
button4.grid(row = 2, column = 0) 
button5 = tk.Button(master = root, text = '停  止', command = tz)
button5.grid(row = 2, column = 1) 
button6 = tk.Button(master = root, text = '右急转', command = yjz)
button6.grid(row = 2, column = 2)
button7 = tk.Button(master = root, text = '退  出', command = tc)
button7.grid(row = 3, column = 1)

tk.mainloop()