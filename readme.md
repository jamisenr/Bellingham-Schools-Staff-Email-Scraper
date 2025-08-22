# This is patched as of the new website update, I am looking for solutions but they seem grim



# Bellingham Schools Staff Email Scraper

This is slightly modified code from my blog post:  
**[How I Scraped Nearly 2,000 Bellingham School District Staff Emails](https://jamisenr.com/blogs/scraping-bellingham-staff-emails)**

It fetches the public HTML staff directory page and extracts any email addresses found in `mailto:` links, saving them to a file (`emails.txt`).

## ⚠ Disclaimer

Use is **at your own ethics and risk**.  
Sending unsolicited bulk email may violate laws in your jurisdiction.  

## Requirements

You need **Python 3.6+** and two packages:  
- [`requests`](https://pypi.org/project/requests/)  
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)  

You can install them using either **APT** (Debian/Ubuntu/Mint) or **pip**.

### Install with APT (Linux)
```bash
sudo apt update
sudo apt install python3-requests python3-bs4
```

### Install with pip (cross-platform)
```bash
pip install requests beautifulsoup4
```

## How to Run

1. **Download** the **main.py** from this repository:

2. **Run the script**:
```bash
python3 main.py
```

3. **Confirm the disclaimer** when prompted.  
   If you choose `n` or `no`, the script will exit.

4. If successful, the script will:
   - Fetch the staff directory page
   - Extract any `mailto:` email addresses
   - Save them to `emails.txt` in the same folder

## Output

- **`emails.txt`** - contains one email per line.
- The script also prints how many emails were found.
