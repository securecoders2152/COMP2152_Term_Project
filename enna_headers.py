# Name: Enna Prudenciano
# Student ID: 101331486
# Vulnerability: Missing Security Headers
# Target: blog.0x10.cloud

import urllib.request


def check_headers():
    target = "http://blog.0x10.cloud"
    print(f"--- Scanning Headers for: {target} ---")

    try:
        # Connecting to the URL request
        response = urllib.request.urlopen(target, timeout=5)
        headers = dict(response.headers)

        # 2. Checking for the missing components
        security_headers = ["Strict-Transport-Security", "Content-Security-Policy", "X-Content-Type-Options"]

        missing = []
        for header in security_headers:
            if header not in headers:
                missing.append(header)

        # 3. Prompt to give report if there's anything missing here
        if missing:
            print(f"BINGO! Found a vulnerability: Some security headers are missing.")
            print(f"The site is currently missing: {', '.join(missing)}")
            print("The risk!: Without these, it's way easier for someone to pull off XSS or Clickjacking attacks.")
        else:
            print("Everything looks good! No missing security headers here. :)")

    except Exception as e:
        print(f"Oops, couldn't connect to the target: {e}")

if __name__ == "__main__":
    check_headers()