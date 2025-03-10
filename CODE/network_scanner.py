
import nmap 
from queue import Queue
import threading

class NetworkScanner:
    def __init__(self):
        self.nm=nmap.PortScanner()
        self.results={}

    def basic_host_discovery(self,host):
        print("host discovery")
        scan_result=self.nm.scan(hosts=host,arguments="-sV -A -T4",sudo=True)
        active_host={}
        for ip, info in scan_result.get("scan",{}).items():
            status = info.get("status",{}).get("state","unknown")
            reason = info.get("reason",{}).get("reason","N/A")
            hostnames = [h['name'] for h in info.get("hostnames",[]) if h['name']]  
            mac = info.get("addresses",{}).get("mac","N/A")
            os = info.get("osmatch",[])

            active_host[ip]={
                "status":status,
                "reason":reason,
                "hostname":hostnames if hostnames else ["None"],
                "mac":mac,
                "os":os if os else ["None"],
            }
        self.results["host"] = active_host
    
    def port_scanning(self,target):
        print("scanning ports")
        self.results["port"]=self.nm.scan(hosts=target,arguments="-sS -sV -p 1-65535 --script=banner",sudo=True)
        print("completed scanning port.....")
    
    def vulnarability_scan(self,target):
        print("scanning for vulnaribilities")
        self.results["vuln"]=self.nm.scan(hosts=target,arguments="--script vuln",sudo =True)
        print("completed scanning vulnaribilities")

    def arp_ping_scan(self, target):
        print("arp ping scanning")
        self.results["ping"]=self.nm.scan(hosts=target,arguments="-PR -sn",sudo =True)
        print("completed arp ping scan")

    def run_threads(self,target):
        threads=[]
        q= Queue()
        task = [
            (self.basic_host_discovery,target),
            (self.port_scanning, target),
            (self.vulnarability_scan,target),
            (self.arp_ping_scan,target),
        ]

        for func, arg in task:
            thread = threading.Thread(target=lambda q,f,a:q.put(f(a)), args=(q,func,arg))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        
    def get_results(self):
        return self.results
    

if __name__== "__main__":
    scanner=NetworkScanner()
    scanner.run_threads("192.168.6.*")
    results=scanner.get_results()

    print("\n port scanning report \n",results.get("port",{}))
    print("\n host scanning report \n",results.get("host",{}))
    print("\n vulnerability scanning report \n",results.get("vuln",{}))
    print("\n ping scanning report \n",results.get("ping",{}))
