# ==========================

# fabiha_http_methods_check.py
# COMP2152 - Term Project
# Name: Fabiha Ishaque
# ID: 101445115

# Vulnerability: Unsafe HTTP Methods Usage
# Target: blog.0x10.cloud

# This script checks if the given URLs are using
# unsafe HTTP methods and prints the result accordingly.

# =========================

import urllib.request
import time

def check_http_methods(url):
    print("=" * 50)
    print("Checking HTTP methods")
    print("=" * 50)

    try:
        # Request the allowed HTTP methods from the server using the OPTIONS method
        request = urllib.request.Request(url, method="OPTIONS")
        response = urllib.request.urlopen(request, timeout=5)

        status = response.status
        allowed_methods = response.getheader("Allow", "")

        print(f"Target URL: {url}")
        print(f"Status: {status}")
        print(f"Allowed Methods: {allowed_methods}")

        unsafe_methods = ["PUT", "DELETE", "TRACE"]
        found = []

        for method in unsafe_methods:
            if method in allowed_methods.upper():
                found.append(method)

        if not allowed_methods:
            # If the 'Allow' header is missing, we cannot determine the allowed methods
            print("\n[WARNING] No 'Allow' header found. Unable to determine allowed HTTP methods.") 
            return 

        if found:
            print("\n[WARNING] Unsafe HTTP methods are enabled.")
            for method in found:
                print(f" - {method}")
                print("This could lead to potential security vulnerabilities.")
        else:
            print("\n[OK] No unsafe HTTP methods are enabled.")  

    except Exception as e:
        print(f"\n[ERROR] Connection failed: {e}")

    print("\n" + "=" * 50)

def main():
    # Check the HTTP methods of the target URL using a delay to prevent getting blocked by the server
    target_url = "http://blog.0x10.cloud"
    time.sleep(0.15)
    check_http_methods(target_url)

if __name__ == "__main__":
    main()