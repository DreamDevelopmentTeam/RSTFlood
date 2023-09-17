from scapy.all import *
from scapy.layers.inet import TCP, IP


def send_tcp_rst_random_source(ip, port):
    src_ip = RandIP()
    src_port = RandShort()
    tcp = TCP(sport=src_port, dport=port, flags="R", seq=0)
    ip = IP(dst=ip, src=src_ip)
    pkt = ip / tcp
    send(pkt, verbose=False)

# 定义一个函数，用于发送TCP RST包
def send_tcp_rst(source_ip, source_port, ip, port):
    # 使用对方的源IP和源端口
    src_ip = source_ip
    src_port = source_port
    # 创建一个TCP包，设置标志位为RST，序列号为随机值，窗口大小为随机值
    tcp = TCP(sport=src_port, dport=port, flags="R", seq=RandInt(), window=RandShort())
    # 创建一个IP包，设置目标IP和源IP，标识符为随机值
    ip = IP(dst=ip, src=src_ip, id=RandShort())
    # 组合IP包和TCP包
    pkt = ip / tcp
    # 发送数据包，并忽略返回值
    send(pkt, verbose=False)

def get_random_IP():
    return RandIP()

def get_random_port():
    return RandShort()