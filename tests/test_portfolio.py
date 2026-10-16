import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.patrickataide.com.br"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_ft001_page_load(driver):
    driver.get(BASE_URL)
    assert "Patrick Ataíde" in driver.title

def test_ft003_technologies(driver):
    driver.get(BASE_URL)
    assert "Playwright" in driver.page_source
    assert "Cypress" in driver.page_source

def test_ft004_contact(driver):
    driver.get(BASE_URL)
    assert "patrickataide.ti@gmail.com" in driver.page_source
