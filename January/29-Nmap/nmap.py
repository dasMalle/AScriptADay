import nmap

nm = nmap.PortScanner()
nm.scan('127.0.0.1', '22-443')
nm.commendline()
nm.scaninfo()