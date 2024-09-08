import requests
import argparse
from termcolor import colored
import re

# Header animasi dengan warna
def print_header():
    header = """
    ███╗   ███╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ███╗██╗███╗   ██╗
    ████╗ ████║██╔══██╗██╔══██╗████╗  ██║██║████╗ ████║██║████╗  ██║
    ██╔████╔██║███████║██████╔╝██╔██╗ ██║██║██╔████╔██║██║██╔██╗ ██║
    ██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╔╝██║██║██║╚██╗██║
    ██║ ╚═╝ ██║██║  ██║██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║██║ ╚████║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝╚═╝   ╚═══╝

    HaOMing_X12 Team: Clan_X12
    """
    print(colored(header, 'cyan'))

# Subdomain finder function
def find_subdomains(domain, wordlist):
    subdomains = []
    with open(wordlist, 'r') as file:
        for line in file:
            subdomain = line.strip()
            url = f"http://{subdomain}.{domain}"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    subdomains.append(f"{subdomain}.{domain} - Found")
            except requests.RequestException:
                continue
    return subdomains

# Main function
def main():
    print_header()

    parser = argparse.ArgumentParser(description='Subdomain Finder Tool')
    parser.add_argument('-f', '--file', type=str, help='File with list of subdomains')
    parser.add_argument('-d', '--domain', type=str, help='Single domain to check')

    args = parser.parse_args()

    if args.file:
        subdomains = find_subdomains(args.domain, args.file)
        if subdomains:
            print("\nSubdomains Found:")
            for subdomain in subdomains:
                print(subdomain)
        else:
            print("No subdomains found.")

    elif args.domain:
        print("Please provide a file with list of subdomains using -f option.")

if __name__ == "__main__":
    main()
