# coding=UTF-8
import optparse
import socket
import threading

def TCPconnect(Host, Port):
    try:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#建立tcp连接
        con.connect((Host, Port))
        print('%d open' % Port)#连接成功则打印出端口号
        con.close()
    except:
        pass

def Scan(Host, low_bound, high_bound):
    try:
        IP = socket.gethostbyname(Host)#解析ip地址
    except:
        print("Cannot resolve '%s': Unknown host" %Host)
        return
    try:
        HostName = socket.gethostbyaddr(IP)
        print('Scan Results for:' + HostName[0])
    except:
        print('Scan Results for:' + IP)
    print('Scan ports %d-%d'%(low_bound, high_bound))
    socket.setdefaulttimeout(1)#设置连接超时时间
    for Port in range(low_bound, high_bound):
         thread = threading.Thread(target=TCPconnect, args=(Host, int(Port)))#多线程
         thread.start()
def main():
    parser = optparse.OptionParser('usage %prog –H <target host> --mn <low_bound> --mx <high_bound>')
    parser.add_option('-H', dest='Host', type='string', help='specify target host')
    parser.add_option('--mn', dest='low_bound', default=0, type='int', help='specify low bound')#输入搜索范围，不输入则搜索默认范围
    parser.add_option('--mx', dest='high_bound', default=1000, type='int', help='specify high bound')
    (options, args) = parser.parse_args()
    Host = options.Host
    low_bound = options.low_bound
    high_bound = options.high_bound
    if (Host == None):
        print('You must specify a target host')
        exit(0)
    Scan(Host, low_bound, high_bound)
if __name__ == '__main__':
    print('scanning…………')
    main()