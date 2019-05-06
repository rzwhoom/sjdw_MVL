# sjdw_MVL视觉定位
## 实验环境
#### Tp_Link路由器 IP(192.168.0.1) SSID(sjsys) PassWord(11111122) 加密方式(WPAPSK_AES)
#### OpenMV_LPB125 IP(192.168.0.2) 波特率115200 TCP_Server 端口8899 STA模式
#### Arduino_LPB125 IP(192.168.0.3) 波特率115200 TCP_Server 端口8899 STA模式
#### 笔记本 IP(DHCP by Tp_Link)
## 实验操作
#### Arduino小车运行xiaoche.ino程序
#### Android手机运行ITEAD-Wifi-Robot程序或笔记本运行ykxc.py，控制Arduino小车运动
#### OpenMV运行gettag.py
#### 笔记本启动Jupyter Lab，运行sjdw.ipynb或者启动Anaconda Prompt，先进入文件夹，然后python sjdw.py
