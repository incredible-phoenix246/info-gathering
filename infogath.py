import socket
import whois
import requests
from bs4 import BeautifulSoup

# Input target domain from the user
domain = input("Enter the target domain: ")

# Domain Information
def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        print("Domain Information:")
        print(domain_info)
    except Exception as e:
        print(f"Error fetching domain information: {str(e)}")

# DNS Footprinting
def dns_footprinting(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"DNS Footprinting - IP Address: {ip_address}")
    except Exception as e:
        print(f"Error performing DNS footprinting: {str(e)}")

# Web Footprinting
def web_footprinting(domain):
    try:
        response = requests.get(f"http://{domain}")
        soup = BeautifulSoup(response.text, "html.parser")
        page_title = soup.title.string
        print(f"Web Footprinting - Page Title: {page_title}")
    except Exception as e:
        print(f"Error performing web footprinting: {str(e)}")

# Network and WHOIS Enumeration
def network_and_whois_enumeration(domain):
    try:
        os.system(f"nslookup {domain}")
    except Exception as e:
        print(f"Error performing network and WHOIS enumeration: {str(e)}")

# Open-Source Intelligence (OSINT)
def osint(domain):
    try:
        # Implement OSINT techniques, e.g., searching for information on public websites, forums, etc.
        print("Open-Source Intelligence (OSINT) - Perform OSINT techniques here.")
    except Exception as e:
        print(f"Error performing OSINT: {str(e)}")

if __name__ == "__main__":
    get_domain_info(domain)
    dns_footprinting(domain)
    web_footprinting(domain)
    network_and_whois_enumeration(domain)
    osint(domain)
