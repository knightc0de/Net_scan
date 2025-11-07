import socket
import time 
import sys
from argparse import ArgumentParser
from termcolor import colored 
from  threading import Thread,Lock

class Net_Scan():

      def __init__(self,ip,start_ports,end_ports,threads=500,verbose=False,proto='tcp'):
          self.proto = proto
          self.ip = ip
          self.start_port = start_ports
          self.end_port = end_ports
          self.thread = threads
          self.verbose = verbose
          self.ports = iter(range(self.start_port, self.end_port + 1))
          self.lock = Lock()
          print(colored((f"[+] Scaning {self.ip}"),"green"))


      def mac_detection():
            pass

      
      def threads_handling(self):
           pro_start_time = time.time()
           thread_list = []
           for _ in range(self.thread):
                thread_list.append(Thread(target=self.scan_ports))
           for thread in thread_list:
                thread.start()  
           for thread in thread_list:
                thread.join()


           pro_end_time = time.time()
           print(colored(f"Scan completed in {pro_end_time - pro_start_time:.2f} seconds","green"))
      
      def scan_ports(self):
       # tcp 
         if self.proto in ('tcp' , 'both') :
           while True:
             try:
                 port = next(self.ports)
             except StopIteration:
                    break  
             try:
                s = socket.socket()
                s.settimeout(1)
                s.connect((self.ip, port))
                with self.lock:
                 print(f"[+] Port {port} is open")
             except PermissionError as e:
                     with self.lock:
                      sys.stderr.write(colored(f"[!] Permission denied on port {port}: {e}\n", "red"))
             except (ConnectionRefusedError, socket.timeout):
                  if self.verbose:
                   with self.lock:
                    sys.stderr.write(colored(f"[-] Port {port} is closed or timed out\n","red"))
                   # sys.exit(1)        
             finally:
                    s.close()

            
            # udp
         if self.proto in ('udp','both'):
             while True:
              try:
                  port = next(self.ports)
              except StopIteration:
                     break  
              try:
                  u = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                  u.settimeout(1.0)
                  try:
                      u.sendto(b'\x00',(self.ip,port)) 
                  except PermissionError as e:
                         with self.lock:
                           sys.stderr.write(colored(f"[!] Permission denied on UDP port {port}: {e}\n","red"))
                         u.close    
                         continue
                  try:  
                      data,addr = u.recvfrom(1024)
                  except socket.timeout:
                      with self.lock:
                          print(colored(f"[-] UDP {port} open filtered (no response)", "yellow"))
                  except ConnectionRefusedError:
                      with self.lock:
                          print(colored(f"[-] UDP port {port} closed ","red"))
                  except OSError as e:
                      with self.lock:
                          print(colored(f"[-] UDP port {port} closed {e}"),"red")                    
                  else:
                      with self.lock:
                          print(colored(f"[+] UDP port {port} is open"),"green")       
              finally:
                   try:
                     u.close()
                   except Exception:
                        pass 


if __name__ == "__main__":
    parser = ArgumentParser(description="Just A Port Scanner",
                            epilog='Example: python %(prog)s -H 192.168.1.10 -s 1 -e 65535 -t 500 -v')

    parser.add_argument("--host", help="Target IPv4", dest="host", required=True)
    parser.add_argument("--proto",help="Protocol to scan: tcp, udp, or both",dest='proto',choices=['tcp', 'udp', 'both'], default='tcp')
    parser.add_argument("-s", help="Starting Port", dest='start_ports', type=int, default=1)
    parser.add_argument("-e", help="Ending Port", dest='end_ports', type=int, default=65535)
    parser.add_argument("-t", help="Number of threads", dest='threads', type=int, default=500)
    parser.add_argument("-v", "--verbose", help="Verbose mode", dest='verbose', action='store_true')
    
    args = parser.parse_args()
    scanner = Net_Scan(args.host, args.start_ports, args.end_ports, args.threads, args.verbose,proto=args.proto)
    scanner.threads_handling()




