import http.client
import os
import dns.resolver



def dns_query(domain,type):
    try:
        f = open('laod.md','w')
        f.close()
        A=dns.resolver.query(domain,type)
        for i in A.response.answer:
            for j in i:
                print (j)
                j = str(j)
                f = open('laod.md','a')
                f.write(j+'\n')   #存储为laod.md文件
                f.close()
    except dns.resolver.NoAnswer:
        print(domain+' 此域名，DNS未响应')



dns_query('cqupt.edu.cn','NS')  # NS记录，标记区域的域名服务器及授权子域；#调用函数
#dns_query('cqupt.edu.cn','A')  # A记录，将主机名转换成IP地址；
#dns_query('cqupt.edu.cn','MX')  # MX记录，邮件交换记录，定义邮件服务器的域名；
#dns_query('cqupt.edu.cn','CNAME')  # CNAME记录，指别名记录，实现域名间的映射；
#dns_query('cqupt.edu.cn','PTR')  # PTR记录，反向解析，与A记录相反，将IP转换成主机名；



