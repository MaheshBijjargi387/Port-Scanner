import socket
import termocolor

def scan(target, ports):
    print('\n'+"Starting scan for"+ str(target))
    for port in range(1,port):
        scan_port(targets,port)


def scan_port(ipaddress, port):
    try:

        sock=socket.socket()
        sock.connect((ipaddress, port))
        print("[+]Port Open"+str(port)) 
        sock.close()


    except:
        pass

targets=input("[*] Enter Target To Scan")     
ports =int(input("[*] Enter How Many Ports You Want To Scan"))
if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targes"),"green")
    print("[*]Scanning Multiple Targets")
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "),ports)

else:
    scan(targets,ports)

scan(target, ports)