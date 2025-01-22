from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

def test():
    driver.get("https://www.google.com/")
    search_input = driver.find_element_by_name("q")
    search_input.send_keys("Python Selenium WebDriver")
    search_input.submit()