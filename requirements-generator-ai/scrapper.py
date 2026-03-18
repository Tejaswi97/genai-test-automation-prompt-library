import requests
from bs4 import BeautifulSoup


def scrape_single_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]

        buttons = []
        for btn in soup.find_all(["button", "a"]):
            text = btn.get_text(strip=True)
            if text and len(text) < 30:
                buttons.append(text)

        inputs = []
        for inp in soup.find_all("input"):
            val = inp.get("name") or inp.get("placeholder") or inp.get("type")
            if val:
                inputs.append(val)

        prices = []
        for text in soup.stripped_strings:
            if "$" in text:
                prices.append(text)

        # Remove duplicates
        headings = list(set(headings))
        buttons = list(set(buttons))
        inputs = list(set(inputs))
        prices = list(set(prices))

        return f"""
--- Page: {url} ---

Title: {title}

Headings:
{', '.join(headings)}

Buttons:
{', '.join(buttons)}

Inputs:
{', '.join(inputs)}

Prices:
{', '.join(prices[:10])}
"""

    except Exception as e:
        return f"\n--- Page: {url} ---\nError: {str(e)}\n"


def scrape_website():
    urls = [
        "https://sauce-demo.myshopify.com/",
        "https://sauce-demo.myshopify.com/account/login",
        "https://sauce-demo.myshopify.com/account/register",
        "https://sauce-demo.myshopify.com/cart"
    ]

    all_content = ""

    for url in urls:
        print(f"Scraping: {url}")
        all_content += scrape_single_page(url)

    return all_content