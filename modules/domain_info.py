import socket
import whois

def get_domain_info(company_name):
    try:
        domain = socket.gethostbyname(company_name)
        whois_data = whois.whois(company_name)
        org = whois_data.get('org', 'N/A')
        return domain, org, whois_data
    except Exception as e:
        return None, None, str(e)