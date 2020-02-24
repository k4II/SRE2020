import sys
import threading
from socket import *


def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        lock.acquire()
        print("Opened Port:", port)
        lock.release()
    # print输出加锁，防止多个输出混合


if __name__=='__main__':
    # scan.py <host> <start_port>-<end_port>
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')

    start_port = int(portstrs[0])
    end_port = int(portstrs[1])

    target_ip = gethostbyname(host)

    lock = thread.allocate_lock()
    #程序启动时创的锁

    for port in range(start_port, end_port):
        p = threading.Thread(target=tcp_test, args=(port,))  # 函数只有一个参数，（port,）表示这个参数为元组
        p.start()