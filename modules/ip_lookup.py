import shodan
from config import SHODAN_API_KEY

def get_shodan_info(ip):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        result = api.host(ip)
        return {
            'IP': result.get('ip_str'),
            'Organization': result.get('org'),
            'Open Ports': result.get('ports'),
            'Hostnames': result.get('hostnames'),
            'CDN Info': result.get('tags')
        }
    except Exception as e:
        return {'Error': str(e)}
