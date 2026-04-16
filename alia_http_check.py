# Author: Alia Qureshi
# Vulnerability: Missing HTTPS Encryption
# Target: blog.0x10.cloud

import urllib.request

try:
    response = urllib.request.urlopen("http://blog.0x10.cloud", timeout=5)

    print("=== Response Info ===")
    print("Status Code:", response.status)
    print("Final URL:", response.url)

    # Check if site is using HTTP instead of HTTPS
    if response.url.startswith("http://"):
        print("\n[VULNERABILITY FOUND]")
        print("This website does NOT use HTTPS.")
        print("Data can be intercepted (man-in-the-middle attack).")
    else:
        print("Site is secure (HTTPS enabled).")

except Exception as e:
    print("Error occurred:", e) 