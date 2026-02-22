import time
from playwright.sync_api import Page, Playwright , expect

from tests.rahulcourse.playwright.utils.apiBase import APIUtils


#api call from browser , api call contact server return back response to browser , browser use response to generate html

#fakePayloadOrderResponse = { "data": [], "message": "No Orders"}
def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0"
    )

def test_netwok_1(page : Page):
    #page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("gabito.onj@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Gabito2025")
    page.get_by_role("button", name="Login").click()
    # go to orders page
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    token = api_utils.getToken(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Inyectar token en localStorage
    context.add_init_script(f"""
        localStorage.setItem('token', '{token}');
    """)

    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

