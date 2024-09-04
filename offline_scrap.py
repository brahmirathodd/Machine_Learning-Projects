import asyncio
import logging
import json
import azure.functions as func
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# Set up Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--enable-logging")
options.add_argument("--v=1")
options.add_argument("--disable-setuid-sandbox")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)
def scrape_data():
# URL of the webpage you want to download
    url = "https://www.flipkart.com/search?q=laptops&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=laptops%7CLaptops&requestId=6824f307-b746-4feb-a674-5d6bab53854b&sort=price_asc&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi7"

    # Navigate to the page
    driver.get(url)

    # Get the HTML content of the page
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    laptops=[]
    laptop_divs = soup.find_all("div", class_="yKfJKb row")
    for laptop_div in laptop_divs:
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

        laptop = {
            'Product Name': product_name,
            'Ratings': ratings,
            'Price': price,
            'Processor': processor,
            'RAM': ram,
            'Operating System': operating_system,
            'ROM': rom,
            'Display': display
        }
        laptops.append(laptop)


    # Close the driver
    driver.quit()

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    laptops = scrape_data()
    return func.HttpResponse(json.dumps(laptops), status_code=200, mimetype='application/json')
