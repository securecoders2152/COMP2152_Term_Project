# Author: Alia Qureshi
# Vulnerability: Open Telnet Port
# Target: telnet.0x10.cloud

import socket

target = "telnet.0x10.cloud"
port = 2323

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    result = sock.connect_ex((target, port))

    if result == 0:
        print("[VULNERABILITY FOUND]")
        print(f"Port {port} is OPEN on {target}")
        print("Telnet is insecure (sends data in plain text).")
    else:
        print("Port is closed.")

    sock.close()

except Exception as e:
    print("Error:", e) 