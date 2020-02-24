import threading
import multiprocessing
import nmap
import time
import sys


def scanHost(network_prefix):
    nm = nmap.PortScannerYield()
    # for rawRes in nm.scan(hosts=network_prefix, ports = portarguments='-sS):
    for rawRes in nm.scan(network_prefix, arguments="-sS"):
    	if 'error' in rawRes[1]['nmap']['scaninfo']:
    		print(rawRes[1]['nmap']['scaninfo']['error'][0])
    		return None
    	for k,v in rawRes[1]['scan'].items():
            try:
                for port, info in v['tcp'].items():
                    if info['state'] == 'open':
                        # print('port {} is open'.format(port))
                        print('tcp/{}'.format(port))
                        print('state:{}'.format(info['state']))
                        print('name:{}'.format(info['name']))
                        print('\n',end='')
                    
            except:
                pass 

            try:
                for port, info in v['udp'].items():
                    if info['state'] == 'open':
                        print('udp/{}'.format(port))
                        print('state:{}'.format(info['state']))
                        print('name:{}'.format(info['name']))
                        print('\n',end='')
            except:
                pass 

def main():
    # po = multiprocessing.Pool(8)
    network_prefix = sys.argv[1]
    # network_prefix = 'www.baidu.com'
    '''
    for i in range(79,88):
        threading.Thread(target=scanHost, args=(network_prefix, str(i), )).start()
        # po.apply_async(scanHost,(network_prefix, str(i), ))
    
    print('----start----')
    po.close()
    po.join()
    print('-----end-----')
    '''
    scanHost(network_prefix)
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start, 's')

