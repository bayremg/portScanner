import socket

def scan():
    ip = input("Enter The IP Address: ")
    portList = [21 , 22 , 23 , 25 , 53 , 80 , 81 , 111 , 137 , 443 , 445]
    print("Scanning [ "+ip+" ]...")
    for port in portList:
        s = socket.socket()
        try:
            s.connect((ip,port))
            print("[+] Port "+str(port)," is OPEN | Service : ",socket.getservbyport(port))

        except:
            print("[!] Port "+str(port)," is CLOSED")

        finally:
            s.close()

    print("[X] Scan Completed...")

scan()
