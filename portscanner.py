import socket
from IPy import IP 


#scan_port() will scan for indivdual ports and will try to grab a banner
def scan_port(ipaddress, port):
    try:
        SOCKET = socket.socket()
        SOCKET.settimeout(0.5)    # timeout is set to 0.5 to make the scans faster. It will wait for 0.5 seconds for the port to respond. if it doesn't respond then the scan will move to next port'
        SOCKET.connect((ipaddress, port))
        
        try:
            banner = get_banner(SOCKET)
            print('Port ' + str(port)  + str(banner)  )
        except:
            print('Port ' + str(port) + ' is open')
           

    except:
        print('Port ' + str(port) + ' is closed')

def check_ip(ip):
    try:
        IP(ip)                    #this function checks if the IP is correct if it is not then it tries to resolve it into its domain name
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def scan_multiple(target):
    converted_ip = check_ip(target)
    print('Scanning ' + str(target))              #this function scans for multiple ports by looping through a given range of ports
    print('\n')
    for port in range(1, 100):              # here it is scanning first 100 ports, the script can be customised to scan only individual ports or a given range of ports
          scan_port(converted_ip, port)


def get_banner(banner):              # this function grabs any response from the port and returns it
     return banner.recv(1024)

target = input('Enter the targets: ')

if ',' in target:
    for ip_address in target.split(','):                     # function calls based on the user input
          scan_multiple(ip_address.strip(' '))

else:
    scan_multiple(target)




