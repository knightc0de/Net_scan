import sys
import scapy.all


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
            ans,unsanswered = srp(self.packet,timeout=1,varbose=False)
            if ans:
               self.ans = ans 
            else: 
                  sys.stderr.write(" no host are up :) ")
                  sys.exit(1)

      def alive_host():
             pass

            
            