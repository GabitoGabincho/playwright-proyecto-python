#Gabito2025
from playwright.sync_api import Playwright, expect

#from tests.rahulcourse.playwright.utils.apiBase import APIUtils
from utils.apiBase import APIUtils

def test_2e2_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context(viewport=None)
    context = browser.new_context()
    page = context.new_page()

    #create order -->orderId
    apiUtils = APIUtils()
    orderID = apiUtils.createOrder(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("gabito.onj@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Gabito2025")
    page.get_by_role("button", name="Login").click()

    #orders history page -> order is present
    # go to orders page
    page.get_by_role("button", name="ORDERS").click()

    # wait table
    page.wait_for_selector("tbody tr")

    # find order
    row = page.locator("tr").filter(has_text=orderID)
    expect(row).to_be_visible(timeout=15000)

    # click view
    row.get_by_role("button", name="View").click()

    # assert thank you page
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    print("Thank you for Shopping With Us")
    context.close()
