# © 2025 Jamisen Renoud - Licensed under the MIT License

import sys
import requests
from bs4 import BeautifulSoup

DISCLAIMER = """\
[NOTICE] This script fetches public HTML and extracts emails from mailto: links.
Use is at your own ethics and risk.
Sending unsolicited bulk email may violate laws in your jurisdiction.
"""

print(DISCLAIMER)
confirm = input("Do you understand and wish to continue? (y/n): ").strip().lower()
if confirm not in ("y", "yes"):
    print("[ABORTED] Exiting script.")
    sys.exit(0)

URL = "https://bellinghamschools.org/wp-content/themes/schoolsites/directoryHandler.php?numPosts=9999999999&pageNumber=1"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

try:
    r = requests.get(URL, headers=HEADERS, timeout=15)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    emails = {
        a["href"].replace("mailto:", "").strip()
        for a in soup.find_all("a", href=True)
        if a["href"].lower().startswith("mailto:")
    }

    with open("emails.txt", "w", encoding="utf-8") as f:
        for email in sorted(emails):
            f.write(email + "\n")

    print(f"[Yippe] Done. {len(emails)} emails saved to emails.txt.")
except Exception as e:
    print(f"[!] Failed: {e}")
