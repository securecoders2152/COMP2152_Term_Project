# ==========================
# fabiha_unauthorized_admin_access.py
# COMP2152 - Term Project
# Name: Fabiha Ishaque
# ID: 101445115
#
# Vulnerability: Unauthorized Access to Admin Pages
#
# This script checks common admin page paths to identify potential
# unauthorized access vulnerabilities. It sends HTTP requests to each path
# and analyzes the response to determine if an admin page is accessible without authentication.
# ==========================

import urllib.request
import urllib.error
import time

def check_admin_pages(target_url, paths):
    print("=" * 60)
    print("Checking for Unauthorized Access to Admin Pages")
    print("=" * 60)

    for path in paths:
        url = target_url + path

        try:
            response = urllib.request.urlopen(url, timeout=5)
            body = response.read().decode(errors="ignore")

            print(f"\nURL: {url}")
            print(f"Status: {response.status}")

            if response.status == 200:
                if "login" not in body.lower():
                    print("[!] VULNERABILITY FOUND")
                    print("Admin page may be accessible without authentication.")
                else:
                    print("[!] Login page detected.")
            else:
                print("[OK] No issue")

        except urllib.error.HTTPError as e:
            print(f"\nURL: {url}")
            print(f"[OK] HTTP {e.code}")

        except Exception as e:
            print(f"\nURL: {url}")
            print(f"[ERROR] {e}")

        time.sleep(0.15)

def main():
    target_urls = [
        "http://0x10.cloud",
        "http://blog.0x10.cloud",
        "http://dev.0x10.cloud",
        "http://test.0x10.cloud",
        "http://api.0x10.cloud"
    ]

    paths = [
        "/admin",
        "/admin/dashboard",
        "/dashboard",
        "/panel",
        "/control",
        "/admin-panel"
    ]

    for target_url in target_urls:
        print("\n" + "=" * 60)
        print(f"Checking URL: {target_url}")
        print("=" * 60)
        check_admin_pages(target_url, paths)

if __name__ == "__main__":
    main()