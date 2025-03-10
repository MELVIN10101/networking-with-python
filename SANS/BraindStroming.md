AI- POWERED SECURITY ANALYSIS TOOLS,'
	->network scanning (nmap integration)
	->Log analysis
		->network
		->ftp
		->data base
		->ssh
rust to python 
method 1 -> local env only
	->maturin build 
		// targets/wheel/name/whl
	->pip install network_scanner-0.1.0-cp313-cp313-linux_x86_64.whl
		// developer can run this to install this in their env
method 2 ->open to everyone
	->pip install twine
	->maturin publish
	->pip install network_scanner




#### **Data Collection Pipeline**

- **Data Sources**:
    
    - Network traffic (packets, flows).
        
    - System logs (firewall, IDS/IPS, endpoints).
        
    - APIs (threat intelligence feeds, cloud services).
        
    - Device information (IPs, MAC addresses, OS fingerprints).
        
- **Data Collection Methods**:
    
    - Packet sniffing (e.g., using `libpnet`).
        
    - Log aggregation (e.g., syslog, Elasticsearch).
        
    - API integrations (e.g., REST, GraphQL).
        
    - Active scanning (e.g., port scanning, vulnerability scanning).