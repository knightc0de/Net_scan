from  requests  import get,exceptions
from  argparse import ArgumentParser,FileType
from  threading import Thread,Lock
from termcolor import colored 
import  time 
import sys

subdomain_list = []

class Subdomain_scan():
      def __init__(self,domain,wordlist,threads=int,verbose=False):
          self.domain = domain 
          self.wordlist = iter(wordlist.read().split())
          self.threads  = threads
          self.verbose = verbose
          self.lock = Lock()
          print(colored("scaning","green"))

      def threads_handling(self):
           pro_start_time = time.time()
           thread_list = []
           for _ in range(self.threads):
              thread_list.append(Thread(target=self.scanning_))
           for threads in thread_list:
               threads.start()
           for threads in thread_list:
               threads.join()
           pro_end_time = time.time()
           print(colored(f"Scan completed in {pro_end_time - pro_start_time:.2f} seconds","green"))
      
      def scanning_(self):
          global subdomain_list 
          while True:
            try:
                with self.lock:
                    word = next(self.wordlist)
            except StopIteration:
                break

            url_https = f"https://{word}.{self.domain}"
            url_http = f"http://{word}.{self.domain}"

            try:
                request = get(url_https, timeout=5)
                if request.status_code == 200:
                    subdomain_list.append(url_https)
                    if self.verbose:
                        print(colored(f"[+] Found: {url_https}","red"))
                    continue
            except (exceptions.RequestException, exceptions.Timeout):
                pass

            try:
                request = get(url_http, timeout=5)
                if request.status_code == 200:
                    subdomain_list.append(url_http)
                    if self.verbose:
                        print(colored(f"[+] Found: {url_http}","red"))
            except (exceptions.RequestException, exceptions.Timeout):
                pass
    
if __name__ == "__main__":
   parser  = ArgumentParser(description="Subdomain Sacnner",epilog="Example : %(prog)s google.com -w worlist.txt -t 500 -v  ")
   parser.add_argument(metavar="domain",help='domain',dest='domain')
   parser.add_argument("-w",help='wordlist',dest='wordlist',type=FileType('r'),default='wordlist.txt')
   parser.add_argument("-t",help='No of Threads',dest='threads',type=int,default=500)
   parser.add_argument("-v",help='Verbose',dest='verbose',action='store_true')
   args = parser.parse_args()

   scanner = Subdomain_scan(args.domain, args.wordlist, args.threads, args.verbose)
   scanner.threads_handling()
   
   
   print(colored("\n[+] Subdomains:","yellow"))
   for sub in subdomain_list:
        print(colored(sub,"green"))

 
       





