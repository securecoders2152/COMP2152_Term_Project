# ============================================================
#  EXAMPLE 2: Check for open ports (Telnet)
#  Target: telnet.0x10.cloud
#  Author: Instructor (starter example)
# ============================================================
#
#  Telnet is an old protocol that sends everything in plain text
#  — including usernames and passwords. Modern servers should
#  NEVER have Telnet open. If a Telnet port is open, that's a
#  security vulnerability.
#
#  This script uses socket.connect_ex() to check if port 2323
#  is open on a target. This is similar to what you built
#  in Assignment 2 (Port Scanner).
#
#  NOTE: Services don't always run on their default port.
#  Real-world scanning means checking non-standard ports too.
# ============================================================

import socket

target = "telnet.0x10.cloud"
port = 2323

print("=" * 50)
print("  Open Port Check (Telnet)")
print("=" * 50)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    print(f"\n  Target: {target}")
    print(f"  Port:   {port}")
    print(f"  Scanning...")

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"\n  [!] VULNERABILITY FOUND")
        print(f"  Port {port} (Telnet) is OPEN on {target}")
        print(f"  Telnet transmits data in cleartext.")
        print(f"  An attacker could intercept credentials.")
    else:
        print(f"\n  [OK] Port {port} is closed on {target}")

    sock.close()

except socket.error as e:
    print(f"\n  [ERROR] Could not connect: {e}")

print("\n" + "=" * 50)
