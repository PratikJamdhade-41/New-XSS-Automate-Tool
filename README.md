# 🔎 Python XSS Vulnerability Scanner

A simple **Python-based web vulnerability scanner** that crawls a website, detects forms, injects XSS payloads, and identifies possible **Cross-Site Scripting (XSS)** vulnerabilities.

This project is designed for **educational and cybersecurity learning purposes**.

---

# 📌 Features

* 🌐 Website crawling
* 🧾 Automatic form detection
* 💉 XSS payload injection
* 🔍 Response analysis
* 📄 JSON vulnerability report generation
* ⚡ Lightweight and beginner friendly

---

# 🧠 How It Works

1. The scanner starts from a **target URL**
2. It **crawls all pages inside the same domain**
3. It **detects forms on each page**
4. Injects an **XSS payload** into form inputs
5. Sends requests to the server
6. Checks if the payload appears in the response
7. If detected, it reports a **possible XSS vulnerability**
8. Saves the result in a **JSON report**

---

# 🛠 Technologies Used

* Python 3
* requests
* BeautifulSoup4
* urllib
* JSON

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/xss-scanner.git
cd xss-scanner
```

Install required packages

```bash
pip install requests beautifulsoup4
```

---

# ▶ Usage

Run the scanner

```bash
python scanner.py
```

Enter the target URL and payload when prompted.

Example:

```
Enter Target URL: http://example.com
Enter XSS Payload: <script>alert(1)</script>
```

---

# 📊 Example Output

```
[*] Crawling: http://example.com
[*] Crawling: http://example.com/login
[!] Possible XSS Found: http://example.com/search

Report saved: xss_report.json
```

---

# 📄 Sample Report

The scanner generates a file called **xss_report.json**

Example:

```json
[
  {
    "url": "http://example.com/search",
    "payload": "<script>alert(1)</script>"
  }
]
```

---

# ⚠ Disclaimer

This tool is developed **only for educational purposes**.

Do **NOT scan websites without permission**.
Unauthorized security testing may be illegal.

Use it only on:

* Your own applications
* Authorized penetration testing environments
* Practice labs (DVWA, OWASP Juice Shop)

---

# 🎓 Learning Purpose

This project helps beginners understand:

* Web crawling
* HTTP requests
* HTML parsing
* Form exploitation
* Basic vulnerability scanning

---

# 🚀 Future Improvements

Possible upgrades:

* Multiple XSS payload testing
* Multithreaded scanning
* SQL Injection detection
* HTML vulnerability reports
* Advanced crawler

---

# 👨‍💻 Author

**Pratik Jamdhade**

Cybersecurity & App Development Student
BCA / MCA

---

⭐ If you like this project, consider giving it a star!
