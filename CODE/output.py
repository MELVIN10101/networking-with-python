from network_scanner import NetworkScanner
import json

def format_output(scan_results):
    """Formats and prints the scan results in a structured way."""
    if not scan_results:
        print("No active hosts found.")
        return

    print("\n🔍 **Scan Results:**\n")
    
    for ip, details in scan_results.items():
        print(f"📌 **IP Address:** {ip}")
        print(f"   🟢 Status: {details['status']} (Reason: {details['reason']})")
        print(f"   🏠 Hostname: {', '.join(details['hostname'])}")
        print(f"   🔍 MAC Address: {details['mac']}")

        os_info = details["os"]
        if os_info != ["None"]:
            print("   🖥️ OS Detection:")
            for os_entry in os_info:
                print(f"     - {os_entry['name']} (Accuracy: {os_entry['accuracy']}%)")
        else:
            print("   ❌ OS Detection: Not Available")

        print("-" * 50)

if __name__ == "__main__":
    scanner = NetworkScanner()  # Initialize scanner
    hosts = scanner.basic_host_discovery("192.168.205.*")# Perform scan
    format_output(hosts)  # Format and display results