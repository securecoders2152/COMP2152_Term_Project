# ==========================

# fabiha_http_check.py
# COMP2152 - Term Project
# Name: Fabiha Ishaque
# ID: 101445115

# Vulnerability: Insecure HTTP Configuration
# Target: blog.0x10.cloud

# This script checks if the given URLs are using
# HTTP or HTTPS and prints the result accordingly.

# =========================

import urllib.request
import time

def check_http_configuration(url):
    print("=" * 50)
    print("Checking HTTP configuration")
    print("=" * 50)

    try:
        # Make a request to the URL and check the response
        response = urllib.request.urlopen(url)
        redirected_url = response.url
        status = response.status

        print(f"Target URL:     {url}")
        print(f"Status:     {status}")
        print(f"Redirected URL:  {redirected_url}")

        if url.startswith("http://") and redirected_url.startswith("https://"):
            print("\n[OK] This redirects to HTTPS.")
            print("The site enforces secure connections.")
        elif url.startswith("http://") and redirected_url.startswith("http://"):
            print("\n[WARNING] This does not redirect to HTTPS.")
            print("The site does not enforce secure connections!")
        else:
            print("\n[OK] The URL is already using HTTPS.")
            print("The site is secure.")
    
    except Exception as e:
        print(f"\n[ERROR] Connection failed: {e}")

    print("\n" + "=" * 50)

def main():
    # Check the HTTP configuration of the target URL using a delay to prevent getting blocked by the server
    target_url = "http://blog.0x10.cloud"
    time.sleep(0.15)
    check_http_configuration(target_url)

if __name__ == "__main__":
    main()