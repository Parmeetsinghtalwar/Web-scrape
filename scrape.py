from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(url):
    chrome_driver_path = "/Users/parmeetsingh/web_founder/chromedriver"  # <-- Update this to your actual chromedriver path
    
    # Initialize Chrome options
    options = Options()
    # Add any options you need, for example:
    # options.add_argument('--headless')  # Uncomment to run Chrome in headless mode
      # ADD THESE OPTIONS:
    options.add_argument('--headless')  # Run in background
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    

    # Create the driver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    driver.get(url)
    
    # ... your scraping logic here ...
    html_content = driver.page_source  # Get the HTML content

    driver.quit()
    return html_content  # <-- Add this line

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]