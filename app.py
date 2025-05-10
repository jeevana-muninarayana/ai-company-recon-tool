from tabulate import tabulate
from modules.domain_info import get_domain_info
from modules.port_scanner import scan_ports
from modules.ip_lookup import get_shodan_info
from modules.recommendations import generate_recommendations

def run_recon(company):
    ip, whois_org, whois_data = get_domain_info(company)
    ports = scan_ports(ip)
    shodan_data = get_shodan_info(ip)
    recs = generate_recommendations(ports, shodan_data.get("CDN Info", []))
    org = shodan_data.get("Organization") or whois_org or "N/A"
    
    # Display results in tables
    print("\n[+] Basic Info:")
    print(tabulate([
        ["Company Domain", company],
        ["IP Address", ip],
        ["Organization", shodan_data.get("Organization", "N/A")],
        ["CDN Info", ', '.join(shodan_data.get("CDN Info", []))],
    ], headers=["Item", "Value"], tablefmt="grid"))

    print("\n[+] Open Ports:")
    print(tabulate([[p] for p in ports], headers=["Port"], tablefmt="fancy_grid"))

    print("\n[+] Security Recommendations:")
    print(tabulate([[r] for r in recs], headers=["Recommendation"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    company = input("Enter company domain (e.g., example.com): ")
    run_recon(company)