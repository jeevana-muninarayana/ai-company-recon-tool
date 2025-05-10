def generate_recommendations(open_ports, cdn_info):
    recs = []

    if 22 in open_ports:
        recs.append("SSH (port 22) is open — restrict access via firewall or use key-based auth with VPN.")
    if 21 in open_ports:
        recs.append("FTP (port 21) is insecure — disable or switch to SFTP.")
    if 25 in open_ports:
        recs.append("SMTP (port 25) is open — ensure proper mail security (SPF, DKIM, DMARC).")
    if 3389 in open_ports:
        recs.append("RDP (port 3389) is open — block or limit to whitelisted IPs, and enforce MFA.")
    if not open_ports:
        recs.append("No common ports found open — good initial posture.")

    if 'cloudflare' not in str(cdn_info).lower():
        recs.append("CDN like Cloudflare not detected — consider using it for DDoS protection and caching.")
    
    recs.append("Regular vulnerability scanning and patching is recommended.")
    recs.append("Consider implementing Web Application Firewall (WAF).")
    recs.append("Enable logging and monitoring for all inbound traffic.")
    recs.append("Use security headers (CSP, HSTS, X-Frame-Options, etc.) in web apps.")

    return recs
