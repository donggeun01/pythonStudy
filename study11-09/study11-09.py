import ipaddress
import socket
import binascii
'''
print(ipaddress.ip_address("172.16.52.174"))
# print(ipaddress.ip_address("fe80::a020:1130:c8e9:37cb%3"))



ADDRESS = {
    '172.16.52.174', 'fe80::a020:1130:c8e9:37cb%3'
}

for ipaddr in ADDRESS :
    addr = ipaddr.ip_address(ipaddr)
    print('IP version:',addr.version)


print(ipaddress.ip_address(3232291687))
print(ipaddress.ip_address(338288524927261089671336703046627436288))



HOSTS = {
    'www.naver.com', 'www.kopo.ac.kr', 'www.python.org', 'testname',
}

for host in HOSTS :
    try :
        print(host, socket.gethostbyname(host)) # 호스트 이름을 문자열주소로 변경

    except socket.error as msg :
        print('예외발생 ', host, msg)


for host in HOSTS :
    print(host)

    try :
        name, aliases, address = socket.gethostbyname_ex(host)
        print(' Hostname', name)
        print(' Aliases :', aliases)
        print(' Addresses:', address)
    except socket.error as emsg :
        print('ERROR', emsg)
    print()

print(socket.getfqdn('kopo.ac.kr'))
print(socket.getfqdn('snu.ac.kr'))
print(socket.getfqdn('www.google.com'))

hostname, aliases, addresses = socket.gethostbyaddr('147.46.10.129')

print('Hostname : ', hostname)
print('Aliases : ', aliases)
print('Address : ', addresses)
'''


HOST = {'www.naver.com','www.google.com',}

for host in HOST :
    print('Host :', socket.gethostbyname(host))
    print('도메인 : ', host)





