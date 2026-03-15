import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json

visited = set()
vulnerabilities = []

def crawl(url, base, payload):
    if url in visited:
        return

    visited.add(url)

    try:
        res = requests.get(url, timeout=5)
    except:
        return

    soup = BeautifulSoup(res.text, "html.parser")

    print("[*] Crawling:", url)

    scan_forms(url, soup, payload)

    for link in soup.find_all("a", href=True):
        new_url = urljoin(base, link["href"])

        if urlparse(new_url).netloc == urlparse(base).netloc:
            crawl(new_url, base, payload)


def scan_forms(url, soup, payload):
    forms = soup.find_all("form")

    for form in forms:
        action = form.get("action")
        method = form.get("method", "get").lower()

        action_url = urljoin(url, action)

        inputs = form.find_all("input")

        data = {}

        for inp in inputs:
            name = inp.get("name")
            if name:
                data[name] = payload

        try:
            if method == "post":
                res = requests.post(action_url, data=data)
            else:
                res = requests.get(action_url, params=data)

            analyze(action_url, payload, res.text)

        except:
            pass


def analyze(url, payload, response):
    if payload in response:
        print("[!] Possible XSS Found:", url)

        vulnerabilities.append({
            "url": url,
            "payload": payload
        })


def save_report():
    with open("xss_report.json", "w") as f:
        json.dump(vulnerabilities, f, indent=4)

    print("\nReport saved: xss_report.json")


if __name__ == "__main__":
    print("XSS Scanner")
    target = input("Enter Target URL: ")
    payload = input("Enter XSS Payload: ")

    crawl(target, target, payload)

    save_report()
