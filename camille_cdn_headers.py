import urllib.request

url = "http://cdn.0x10.cloud/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req) as response:
        h = dict(response.headers)

        print("--- CDN Vulnerability Report ---")

        leaks = [h.get("x-forwarded-for"), h.get("x-cache"), h.get("via")]
        for leak in leaks:
            if leak and "10." in leak:
                print(f"[!] VULNERABILITY: Internal IP Leak detected: {leak}")

        backend = h.get("x-backend-server")
        if backend:
            print(f"[!] VULNERABILITY: Internal Hostname Disclosure: {backend}")

        timing = h.get("Server-Timing")
        if timing:
            print(f"[!] VULNERABILITY: Server-Side Timing Leak: {timing}")

except Exception as e:
    print(f"Request failed: {e}")
