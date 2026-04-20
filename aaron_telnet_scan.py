# Name: Aaron Balayo
# Student ID: 101575606
# Vulnerability: Open Telnet Port
# Target: telnet.0x10.cloud:2323
# Description: Telnet service is exposed on a non-standard port and transmits all data in cleartext.

# ==========================================

# Vulnerability Title: Open Telnet Port on port 2323
# Description: Telnet service is running on telnet.0x10.cloud:2323. Telnet doesn't encrypt traffic, which allows anyone to intercept usernames and passwords.

# ==========================================

import socket

target = "telnet.0x10.cloud"
port = 2323

print(f"Scanning {target} on port {port}...")

try:
    # Create socket -> set short timeout
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    # Trying to connect to port
    result = sock.connect_ex((target, port))

    if result == 0:
        print("VULNERABILITY FOUND: Port 2323 (Telnet) is OPEN on telnet.0x10.cloud")
        print("Security Risk: Telnet sends usernames, passwords, and all commands in plain text.")
        print("An attacker on the same network can easily sniff and steal credentials.")
    else:
        print(f"Port {port} is closed / filtered.")

except Exception as e:
    print(f"Error scanning {target}:{port} - {e}")
finally:
    sock.close()

print("\nScan completed.")