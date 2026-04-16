# Author: Member Name
# Vulnerability: Server Info Disclosure
# Target: api.0x10.cloud

import urllib.request

try:
    response = urllib.request.urlopen("http://api.0x10.cloud", timeout=5)
    headers = dict(response.headers)

    print("=== Headers ===")
    for key, value in headers.items():
        print(f"{key}: {value}")

    if "Server" in headers:
        print("\n[VULNERABILITY FOUND]")
        print("Server version is exposed:", headers["Server"])
        print("Attackers can use this info to exploit known vulnerabilities.")

except Exception as e:
    print("Error:", e) 