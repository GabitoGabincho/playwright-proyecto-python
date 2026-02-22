#https://rahulshettyacademy.com/angularpractice/shop
import time

from playwright.async_api import expect
from playwright.sync_api import  Page

def test_UIValidationDynamicScript(page:Page):
    #iphoneX  Nokia Edge  -> 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")  # correcta
    page.get_by_role("combobox").select_option("teach")  # combox
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()  # button
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    #collect all the card  4 cards - select filter has text with this text and bring the component
    #iphoneProduct.locator()
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout")
    #expect(page.locator(".media-body"))
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(10)

def test_childWindowsHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click() #new page child
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)
        #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at") #0 --> please email us . 1 mentor@rahulshettyacademy.com with below template to receive response
        #email = words[1].split("")[0] #0 -> mentor@rahulshettyacademy.com 1-> with below template to receive response
        #email = words[1].split(" ")[1] #ok
        email = words[1].strip().split(" ")[0] #ok
        time.sleep(10)
        print(email)
        assert email == "mentor@rahulshettyacademy.com"