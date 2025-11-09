import sys
import scapy.all


class Mac_detect():
      def __init__(self,host):
            self.host = host 
      
      def packet(self):
            layer_1 = Ether(dst="ff:ff:ff:ff:ff:ff")
            layer_2 = ARP()

            
            