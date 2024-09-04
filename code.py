'''
import logging
import azure.functions as func
import requests
from bs4 import BeautifulSoup
import time

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    results = []
    for i in range(1, 10):
        url = f"https://www.flipkart.com/search?q=laptops&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=laptops%7CLaptops&requestId=6824f307-b746-4feb-a674-5d6bab53854b&as-searchtext=laptops&page={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        laptop_divs = soup.find_all("div", class_="yKfJKb row")

        for laptop_div in laptop_divs:
            product_name = ""
            ratings = ""
            price = ""
            processor = ""
            ram = ""
            operating_system = ""
            rom = ""
            display = ""

            try:
                product_name = laptop_div.find("div", class_="KzDlHZ").text.strip()
            except:
                product_name = ""

            try:
                ratings = laptop_div.find("div", class_="_5OesEi").text.strip()
            except:
                ratings = ""

            try:
                price = laptop_div.find("div", class_="Nx9bqj _4b5DiR").text.strip()
            except:
                price = ""

            try:
                specs_div = laptop_div.find("div", class_="_6NESgJ")
                specs = specs_div.find_all("li", class_="J+igdf")
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
            except:
                pass

            results.append({
                "Product Name": product_name,
                "Ratings": ratings,
                "Price": price,
                "Processor": processor,
                "RAM": ram,
                "Operating System": operating_system,
                "ROM": rom,
                "Display": display
            })

        # Sleep between requests to avoConda env remove --name (name of the env)id overloading the serverpip
        time.sleep(1)

    return func.HttpResponse(str(results))
'''
import logging
import json
import azure.functions as func
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import concurrent.futures

def scrape_page(i):
    laptops = []
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    success = False
    while not success:
        try:
            url = f"https://www.flipkart.com/search?q=laptops&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=laptops%7CLaptops&requestId=896da398-392d-4f33-96e7-ac94efd1b3de&as-searchtext=laptops&page={i}"
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')

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
            success = True

        except Exception as e:
            logging.error(f"An error occurred while scraping page {i}: {e}")
            time.sleep(0)  # Wait for 10 seconds before retrying

    driver.quit()
    return laptops

def scrape_and_get_laptops():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_to_page = {executor.submit(scrape_page, i): i for i in range(1, 33)}
        all_laptops = []
        for future in concurrent.futures.as_completed(future_to_page):
            all_laptops.extend(future.result())
    return all_laptops

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    laptops = scrape_and_get_laptops()
    return func.HttpResponse(json.dumps(laptops), status_code=200, mimetype='application/json')

# Entry point for the Azure function
def init_func(func: func.HttpRequest):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(func))

 # type: ignore