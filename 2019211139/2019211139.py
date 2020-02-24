import socket
def scan_port(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip, port))
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip, port))
    finally:
        server.close()
print('请问您需要哪种扫描方式？'+'\n1：按个扫描该IP各个端口'+'\n2：单个扫描您指定的端口类型'+'\n（端口号超过100请选2）')
a=int(input('您的选择是：'))
ip=str(input('请输入IP或域名:'))
if a==1:
    if __name__ == '__main__':
        for port in range(24, 100):
            scan_port(ip, port)
if a==2:
    port=int(input('请输入端口号:'))
    if __name__ == '__main__':
        scan_port(ip, port)
else:
    print('输入错误，请重新启动并输入1或2')