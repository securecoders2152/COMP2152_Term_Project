import urllib.request
import urllib.error

url = "http://cdn.0x10.cloud/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})


def check_headers(h):
    print("--- CDN Vulnerability Report ---")

    for header in ["x-forwarded-for", "x-cache", "via"]:
        value = h.get(header)
        if value and "10." in value:
            print(f"[!] VULNERABILITY: Internal IP Leak in '{header}': {value}")

    backend = h.get("x-backend-server")
    if backend:
        print(f"[!] VULNERABILITY: Internal Hostname Disclosure: {backend}")

    timing = h.get("server-timing")
    if timing:
        print(f"[!] VULNERABILITY: Server-Side Timing Leak: {timing}")

    server = h.get("server")
    if server and any(v in server.lower() for v in ["apache/", "nginx/", "iis/"]):
        print(f"[!] VULNERABILITY: Server Version Disclosure: {server}")

    for header in [
        "x-frame-options",
        "x-content-type-options",
        "content-security-policy",
    ]:
        if not h.get(header):
            print(f"[!] MISSING HEADER: {header}")


try:
    with urllib.request.urlopen(req) as response:
        check_headers(dict(response.headers))

except urllib.error.HTTPError as e:

    print(f"[i] Server returned HTTP {e.code} — checking headers anyway")
    check_headers(dict(e.headers))

except Exception as e:
    print(f"Request failed: {e}")
