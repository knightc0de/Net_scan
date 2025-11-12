from prettytable import PrettyTable
from mac_vendor_lookup import MacLookup
from  scapy.all import  ARP, Ether, srp 
import sys 

class Mac_detect():
      def __init__(self,host):
            self.host = host 
            self.host_alive  = {}
      def packet(self):
            layer_1 = Ether(dst="ff:ff:ff:ff:ff:ff")
            layer_2 = ARP(pdst=self.host)
            packet = layer_1 / layer_2 
            self.packet = packet
      
      def send_packet(self):
            ans,unsanswered = srp(self.packet,timeout=1,verbose=False)
            if ans:     
               self.ans = ans 
            else: 
                  sys.stderr.write(" no host are up :) ")
                  sys.exit(1)

      def alive_host(self):
             for sent,ans in self.ans:
                 self.host_alive[ans.psrc] = [ans.hwsrc]
                  
      def print_alive(self):
          table = PrettyTable(["IP","MAC","VENDOR"])
          for ip,mac in self.host_alive.items():
             try:
                  table.add_row([ip,mac,MacLookup(mac)])
             except:
                  table.add_row([ip,mac,"UNKOWN"])
          print(table)
            
scan = Mac_detect("192.168.1.0/24")   
scan.packet()
scan.send_packet()
scan.alive_host()
scan.print_alive()