# -*- coding:utf-8 -*-
import csv, matplotlib, os, win32api
import pandas as pd
import numpy as np
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示matplotlib中文
zt = ('SimHei', 24)    #定义字体字号
bbox_style = dict(boxstyle = 'rarrow', fc = 'white', ec = 'blue', lw = 3) #定义文本样式,显示坐标和角度

def dwstart():
    button1['state'] = tk.DISABLED #button1不可用
    button2['state'] = tk.NORMAL   #button2可用
    #添加外部执行zuobiao.py代码
    win32api.ShellExecute(0, 'open', r'zuobiao.py', '', '', 1)

def dwend():
    button1['state'] = tk.NORMAL   #button1可用
    button2['state'] = tk.DISABLED #button2不可用
    #添加外部关闭zuobiao.py代码
    os.system('taskkill /F /IM py.exe')
    
def dwquit():
    with open(r'data\zuobiao.csv', 'w', newline = '') as f1:
        w = csv.writer(f1)
        w.writerow(['id', 'xd', 'yd', 'jiaodu', 'i']) #清空zuobiao.csv
    root.quit()     # GUI对象停止循环
    root.destroy()  # 彻底消除GUI对象

def sjzb():
    sj = pd.read_csv(r'data\zuobiao.csv')    #使用pandas打开csv文件，sj为DataFrame
    sj_droped = sj.dropna(axis = 0)          #丢弃有缺失值的行
    sj_id0 = sj_droped[sj_droped['id'] == 0] #得到id为0的数据，类型为dataframe
    xs = sj_id0['xd']     #取出xd列，类型为Series
    ys = sj_id0['yd']     #取出yd列
    sj_1 = sj_id0.tail(1) #取出最后一行，类型为Series

    #sj_30 = sj_id0.tail(30) #取出最后30条记录，类型为DataFrame
    #xs = sj_30['xd'] #取出xd列，类型为Series
    #ys = sj_30['yd'] #取出yd列
    #以上为减轻计算负担，画面可以只显示最近的若干个点
    return xs, ys, sj_1
    
def animate(i):
    a.clear()         #刷新图像，包括相关设置
    good_sj = sjzb()  #获取函数返回值
    xs = good_sj[0]   #获取xd列
    ys = good_sj[1]   #获取yd列
    sj_1 = good_sj[2] #获取最后一行
    try:
        x = int(sj_1['xd'].values)      #通过字段索引转换后得到横坐标
        y = int(sj_1['yd'].values)      #得到纵坐标
        jd = int(sj_1['jiaodu'].values) #得到角度值
        a.plot(xs, ys, color = 'orange', linewidth = 2, zorder = 20) 
        #折线图轨迹绘制, zoder为图层, 可以加入marker = '.', 显示每一个数据点
        a.text(x, y, '   ', size = 8, zorder = 30, rotation = jd, bbox = bbox_style) #方向显示
        a.text(320, 500, '实时x坐标：'+str(x)+';  实时y坐标：'+str(y)+';  实时θ角度：'+str(jd), size = 8)
    except(TypeError): #防止zuobiao.csv为空
        pass
    
    a.set_xlim(0, 640) #x刻度范围
    a.set_ylim(0, 520) #y刻度范围
    a.grid(False)      #显示网格
    a.xaxis.set_ticks_position('top') #x轴上移
    a.invert_yaxis()                  #y轴反向
    a.set_aspect('equal')             #固定纵横比例
    a.plot([0, 640], [480, 480], linewidth = 0.5, color = 'black')

root = tk.Tk()
root.wm_title('基于机器视觉的定位与导航_视觉定位') #窗口标题栏设置
root.iconbitmap('tb.ico')                       #窗口标题栏图标
root.geometry('960x800+960+0')                  #窗口大小及位置
root.resizable(width = False, height = False)   #固定窗口大小

fig = Figure(figsize = (9.6, 7.2), dpi = 100)   #设置图像大小
a = fig.add_subplot(111)
a.set_facecolor('whitesmoke')

canvas = FigureCanvasTkAgg(fig, master = root) #在canvas画布控件中添加fig对象
canvas.draw()
canvas.get_tk_widget().grid(row = 2, column = 0, columnspan = 7) #使用grid定位，第三行，第一列，横跨7列（合并第三行）

label = tk.Label(master = root, text = '视觉定位', font = zt)            #添加标签对象
label.grid(row = 0, column = 0, pady = 20, padx = 10, columnspan = 7)   #使用grid定位，第一行，第一列，横跨7列（合并第一行）
button1 = tk.Button(master = root, text = '开始定位', command = dwstart) #添加按钮对象
button1.grid(row = 1, column = 2) #使用grid定位，第二行，第三列
button2 = tk.Button(master = root, text = '停止定位', command = dwend)
button2.grid(row = 1, column = 3) #使用grid定位，第二行，第四列
button2['state'] = tk.DISABLED    #button2不可用
button3 = tk.Button(master = root, text = '退出程序', command = dwquit)
button3.grid(row = 1, column = 4) #使用grid定位，第二行，第五列

ani = animation.FuncAnimation(fig, animate, interval = 100) #添加动画
tk.mainloop()