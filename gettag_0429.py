# -*- coding:utf-8 -*-
import sensor, image, time, math, json
from pyb import UART                   #加载串口库文件
uart = UART(3, 115200)                 #默认3口，波特率115200，P4为Tx，P5为Rx
sensor.reset()                         #摄像头重置
sensor.set_pixformat(sensor.GRAYSCALE) #使用灰度，非VGA也可以sensor.RGB565
sensor.set_framesize(sensor.VGA)       #VGA：640*480；QVGA：320*240；QQVGA：160*120
sensor.skip_frames(time = 2000)        #延时，待镜头稳定
sensor.set_auto_gain(False)            #关闭自动增益
sensor.set_auto_whitebal(False)        #关闭自动白平衡
clock = time.clock()                   #建立计时对象
i = 0                                  #建立计数对象
area = [(0,0,240,180), (200,0,240,180), (400,0,240,180), (0,150,240,180), (200,150,240,180),
        (400,150,240,180), (0,300,240,180), (200,300,240,180), (400,300,240,180)]
                                       #第一次需要分区带重合扫描得到目标坐标和下一次扫描画面的起始坐标
                                       #每个分区大小为240*180，已是实验最优值。

while(True):
    flag = 0                           #设置捕获标记，起始为0
    for a in area:                     #历遍所有分区
        sensor.set_windowing(a)        #设置扫描区域
        clock.tick()                   #帧率计时，仅为笔记本查看帧率需要
        img = sensor.snapshot()        #获取画面

        for tag in img.find_apriltags(families = image.TAG36H11):  #在画面中找到AprilTag对象
            img.draw_rectangle(tag.rect(), color = (255, 0, 0))    #画出Tag区域，仅为笔记本查看需要
            img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))#画出Tag中心，仅为笔记本查看需要
            cx = tag.cx()+a[0]         #得到真实画面横坐标
            cy = tag.cy()+a[1]         #得到真实画面纵坐标
            taglist = []               #建立空列表
            taglist.append(tag.id())   #列表中加入id
            taglist.append(cx)         #列表中加入真实画面横坐标
            taglist.append(cy)         #列表中加入真实画面纵坐标
            taglist.append(int(tag.rotation()*180/math.pi))
                                       #列表中加入角度
            taglist.append(i)          #列表中加入计数
            uart.write(json.dumps(taglist)+'\n') #将列表转为json字符串格式通过串口发送
            print(taglist)             #打印列表，仅为笔记本查看需要
            i = i+1                    #计数更新
            if cx < 120:
                ax = 0
            elif cx > 520:
                ax = 400
            else:
                ax = cx-120
            if cy < 90:
                ay = 0
            elif cy > 390:
                ay = 300
            else:
                ay = cy-90             #设置ax，ay为下一次扫描区域的起始坐标
            flag = 1                   #设置捕获标记为1
            print(clock.fps())         #打印帧率，仅为笔记本查看帧率需要

    if (flag == 0):                    #若未得到AprilTag对象，继续分区带重合扫描
        area = [(0,0,240,180), (200,0,240,180), (400,0,240,180), (0,150,240,180), (200,150,240,180),
            (400,150,240,180), (0,300,240,180), (200,300,240,180), (400,300,240,180)]
    else:
        area = [(ax, ay, 240, 180)]    #否则的话重新设定扫描区域，进行追踪扫描
    #time.sleep(100)
