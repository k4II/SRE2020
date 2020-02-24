import dns.resolver
import datetime
import os

class SubDomainScan:
    def __init__(self, target):
        self.domain = target
        self.subdomains = []
        self.subs = []
        with open('subs.txt','r') as f:
            for sub in f.readlines():
                sub = sub.strip()
                self.subs.append(sub)
        for sub in self.subs:
            self.subdomains.append('{sub}.{domain}'.format(sub=sub,domain=self.domain))

    def DNSQuery(self):#通过DNS请求判断子域名是否存在，不支持泛解析
        self.subdomains_success = []
        for domain in self.subdomains:
            try:
                dns.resolver.query(domain,'A')
                self.subdomains_success.append(domain)
            except Exception as e:
                continue

    def OnlineCheck(self):#使用ping检测列表中的域名对应主机是否在线
        print('Detecting........')
        for domain in self.subdomains_success:
            response = os.system("ping -c 1 " + domain + " > /dev/null 2>&1")
            if response == 0:
                i = self.subdomains_success.index(domain)
                self.subdomains_success[i] = domain + '------ONLINE'
            else:
                continue

    def SaveResult(self):#保存结果到本地
        self.path = './{domain}_{time}.txt'.format(domain=domain, time=datetime.datetime.now().strftime("%Y-%m_%d_%H-%M"))
        with open(self.path,'w+') as f:
            for line in self.subdomains_success:
                f.write(line+'\n')



domain = input("please input domain: ")
s = SubDomainScan(domain)
print('Scaning........')
s.DNSQuery()
print('Found ' + str(len(s.subdomains_success)) + ' subdomains')
isOnlineCheckNeeded = input("Do you want to check online status?(y/n)")
if isOnlineCheckNeeded == 'y':
    s.OnlineCheck()
s.SaveResult()
print('Finished!')
print('Result stored in ',s.path)