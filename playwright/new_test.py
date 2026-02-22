import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport=None)
    page = context.new_page()
    page.goto("https://google.com")
    input("Enter para cerrar")
    time.sleep(10)