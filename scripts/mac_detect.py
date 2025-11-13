from prettytable import PrettyTable
from mac_vendor_lookup import MacLookup
from  scapy.all import  ARP, Ether, srp 
import sys 

class Mac_detect():
      def __init__(self,host):
            self.host = host 
            self.alive_hosts  = {}
      def packet(self):
        try:
            layer_1 = Ether(dst="ff:ff:ff:ff:ff:ff")
            layer_2 = ARP(pdst=self.host)
            packet = layer_1 / layer_2 
            self.packet = packet
        except Exception as e:
              sys.stderr.wrie(f"[!] Fail to build ARP packet {e}")
              sys.exit(1)         
    
      def send_packet(self):
        try:
             ans,unsanswered = srp(self.packet,timeout=1,verbose=False)
        except PermissionError:
               sys.stderr.write(
                    "[!] Permission denied run as root "
               )    
               sys.exit(1)
        except Exception as e:
            sys.stderr.write(f"[!] Error sending ARP request: {e}\n"
                             )
            sys.exit(1)

        if ans:     
            self.ans = ans 
        else:         
            sys.stderr.write(" no host are up :) ")
            sys.exit(0)

      def alive_host(self):
             for sent,ans in self.ans:
                 self.alive_hosts[ans.psrc] = [ans.hwsrc]
                  
      def vendor_(self,mac):
           mac_lookup = MacLookup()

           try:
                vendor = mac_lookup.lookup(mac)  
                return vendor 
          
           except VendorNotFoundError:
               try:
                    print(f"[!] Vendor not found for {mac} :( ")
                    mac_lookup.update_vendors()
                    vendor = mac_lookup.lookup(mac)
                    return vendor 
               except Exception:
                    return "UNkNOWN"

           except Exception:
                return "UNKNOWN"                           
                        
      def print_alive(self):
          table = PrettyTable(["IP","MAC","VENDOR"])
          table.align["IP"] = "1"
          table.align["MAC"] = "1"
          table.align["VENDOR"] = "1"

          if not self.alive_hosts:
               print("[!] No hosts are found")

          for ip,mac in self.alive_hosts.items():
                  vendor = self.lookup_vendor(mac)
                  table.add_row([ip,mac,vendor])

          print("\n" + "=" * 65)
          print(" Mac ADDr DETECTION ")
          print("=" * 65)
          print(table)
          print( "=" * 65 + "\n")
            
scan = Mac_detect("192.168.1.0/24")   
scan.packet()
scan.send_packet()
scan.alive_host()
scan.print_alive()