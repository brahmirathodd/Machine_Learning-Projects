import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

laptops = []

async def fetch_data(url, session):
    async with session.get(url) as response:
        return await response.text()

def process_page(content):
    if not content:
        return

    try:
        soup = BeautifulSoup(content, 'html.parser')
        laptop_divs = soup.find_all("div", class_="yKfJKb row")

        for laptop_div in laptop_divs:
            try:
                product_name = laptop_div.find("div", class_="KzDlHZ").text.strip() if laptop_div.find("div", class_="KzDlHZ") else ""
                ratings = laptop_div.find("div", class_="_5OesEi").text.strip() if laptop_div.find("div", class_="_5OesEi") else ""
                price = laptop_div.find("div", class_="Nx9bqj _4b5DiR").text.strip() if laptop_div.find("div", class_="Nx9bqj _4b5DiR") else ""
                specs_div = laptop_div.find("div", class_="_6NESgJ")
                specs = specs_div.find_all("li", class_="J+igdf") if specs_div else []
                processor, ram, operating_system, rom, display = "", "", "", "", ""

                for spec in specs:
                    spec_text = spec.text.lower()
                    if "processor" in spec_text:
                        processor = spec_text
                    elif "ram" in spec_text:
                        ram = spec_text
                    elif "operating" in spec_text:
                        operating_system = spec_text
                    elif "hdd" in spec_text or "ssd" in spec_text:
                        rom = spec_text
                    elif "display" in spec_text:
                        display = spec_text

                laptops.append({
                    "Product_Name": product_name,
                    "Ratings": ratings,
                    "Price": price,
                    "Processor": processor,
                    "RAM": ram,
                    "Operating System": operating_system,
                    "ROM": rom,
                    "Display": display
                })
            except Exception as e:
                print(f"Error processing a laptop div: {e}")
    except Exception as e:
        print(f"Error processing page content: {e}")

async def scrape_laptops_async(url):
    async with ClientSession() as session:
        html_content = await fetch_data(url, session)
        process_page(html_content)

# Endpoint to trigger scraping
@app.route('/scrape/laptops')
async def trigger_scraping():
    laptops.clear()  # Reset laptops list before scraping

    tasks = []
    for i in range(1, 83):
        url = f"https://www.flipkart.com/search?q=laptops&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=laptops%7CLaptops&requestId=896da398-392d-4f33-96e7-ac94efd1b3de&as-searchtext=laptops&page={i}"
        tasks.append(scrape_laptops_async(url))

    await asyncio.gather(*tasks)
    return jsonify(laptops)

if __name__ == '__main__':
    app.run(debug=False)


