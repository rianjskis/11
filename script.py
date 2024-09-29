import requests

def fetch_and_convert_github_hosts(github_raw_url):
    # Fetch the file content from GitHub
    response = requests.get(github_raw_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch file from GitHub: {response.status_code}")

    all_domain = []
    hosts_data = response.text.splitlines()  # Read file line by line

    for line in hosts_data:
        # Skip comments and empty lines
        if line.startswith('#') or not line.strip() or '127.0.0.1' in line:
            continue
        
        parts = line.split()
        if len(parts) >= 2:  # Only take the first two columns, ignore extra columns
            ip, domain = parts[:2]
            all_domain.append(domain)

    return all_domain  # Return the list of domains

# Example GitHub hosts file link
github_raw_url = "https://raw.githubusercontent.com/lingeringsound/10007_auto/master/reward"

# Fetch and convert the hosts file
all_domains = fetch_and_convert_github_hosts(github_raw_url)

# Write the results to a .srs file
with open('singbox_rules.srs', 'w') as outfile:
    for domain in all_domains:
        outfile.write(f"{domain}\n")  # Directly write the domain
