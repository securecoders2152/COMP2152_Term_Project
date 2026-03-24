# ============================================================
#  EXAMPLE 3: Inspect HTTP response headers
#  Target: api.0x10.cloud, cdn.0x10.cloud
#  Author: Instructor (starter example)
# ============================================================
#
#  HTTP response headers can leak sensitive information:
#  - Server version (tells attackers what exploits to try)
#  - Internal IP addresses (reveals network topology)
#  - Missing security headers (allows clickjacking, XSS, etc.)
#
#  This script shows how to read response headers using urllib.
#  Many vulnerabilities on 0x10.cloud are hidden in headers,
#  not in the page content!
#
#  Technique: Use urllib to make a request, then inspect the
#  response headers dictionary for sensitive information.
# ============================================================

import urllib.request

print("=" * 50)
print("  HTTP Header Inspection")
print("=" * 50)

# --- Check 1: Server version disclosure ---

target = "http://api.0x10.cloud"
print(f"\n  [1] Checking {target} for server version leak...")

try:
    response = urllib.request.urlopen(target, timeout=5)
    headers = dict(response.headers)

    server = headers.get("Server", "Not disclosed")
    powered_by = headers.get("X-Powered-By", "Not disclosed")

    print(f"      Server:       {server}")
    print(f"      X-Powered-By: {powered_by}")

    if server != "Not disclosed" or powered_by != "Not disclosed":
        print("\n  [!] VULNERABILITY FOUND")
        print("  Server version is exposed in HTTP headers.")
        print("  Attackers can look up known exploits for this version.")
    else:
        print("\n  [OK] No server version leaked in headers.")

except Exception as e:
    print(f"  [ERROR] {e}")


# --- Check 2: Internal IP leak in headers ---

target2 = "http://cdn.0x10.cloud"
print(f"\n  [2] Checking {target2} for internal IP leak...")

try:
    response2 = urllib.request.urlopen(target2, timeout=5)
    headers2 = dict(response2.headers)

    # These headers sometimes contain internal/private IP addresses
    interesting = ["X-Forwarded-For", "X-Real-IP", "X-Backend-Server", "Via"]
    found = []

    for h in interesting:
        val = headers2.get(h, "")
        if val:
            found.append(f"{h}: {val}")

    if found:
        print("      Headers with potential internal info:")
        for f in found:
            print(f"        {f}")
        print("\n  [!] VULNERABILITY FOUND")
        print("  Internal IP addresses are exposed in response headers.")
        print("  This reveals the internal network layout to attackers.")
    else:
        print("  [OK] No internal IPs found in headers.")

except Exception as e:
    print(f"  [ERROR] {e}")

print("\n" + "=" * 50)
