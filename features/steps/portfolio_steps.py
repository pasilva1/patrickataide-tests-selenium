from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.patrickataide.com.br"

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

@given('que acesso o site')
def step_access_site(context):
    context.driver = get_driver()
    context.driver.get(BASE_URL)

@then('o título deve conter "{title}"')
def step_title(context, title):
    assert title in context.driver.title
    context.driver.quit()

@then('deve exibir as tecnologias Playwright e Cypress')
def step_tech(context):
    content = context.driver.page_source
    assert "Playwright" in content
    assert "Cypress" in content
    context.driver.quit()

@then('o e-mail de contato deve estar visível')
def step_email(context):
    content = context.driver.page_source
    assert "patrickataide.ti@gmail.com" in content
    context.driver.quit()
