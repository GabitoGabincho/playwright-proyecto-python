#HOW TO INTERCEPT RESPONSES

import time

from playwright.sync_api import Page, Playwright


#api call from browser , api call contact server return back response to browser , browser use response to generate html

fakePayloadOrderResponse = { "data": [], "message": "No Orders"}
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )


def test_netwok_1(page : Page):
    #page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("gabito.onj@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Gabito2025")
    page.get_by_role("button", name="Login").click()

    # go to orders page
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(10)
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
