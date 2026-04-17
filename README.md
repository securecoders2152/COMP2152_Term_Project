# COMP2152 — Term Project: CTF Bug Bounty

## Team Name
securecoders2152

## Team Members

| Member | Vulnerability Found | Branch Name |
|--------|-------------------|-------------|
| Alia Qureshi (101535665) | Missing Security Headers / HTTP / Port Scan | alia_vulnerabilities |
| Aaron Balayo (101575606) | Open Telnet Port (Port Scan) | aaron_telnet_scan |
| Camille Yu (101568394) | HTTP instead of HTTPS | camille_http_check |
| Enna Prudenciano (101331486) | Missing Security Headers | enna_headers |
| Fabiha Ishaque (101535665) | Insecure HTTP Configuration | fabiha_http |

## Videos

- Alia: https://youtu.be/SfAlUg2tEy4?si=YVp2i9te1MeE7LRm 
- Aaron: https://youtu.be/1B-A6YrDxn4
- Camille: https://youtu.be/A2-gkCTeq-Q?feature=shared 
- Enna: https://youtube.com/watch?v=________
- Fabiha: https://youtube.com/watch?v=________

## Target

- Server: `0x10.cloud` and its subdomains
- Submission: http://submit.0x10.cloud
- Leaderboard: http://ranking.0x10.cloud

## Important: Rate Limit

The server allows **10 requests per second** per IP address. If you send requests too fast, you will get blocked (HTTP 429). Add a small delay between requests:

```python
import time
time.sleep(0.15) 