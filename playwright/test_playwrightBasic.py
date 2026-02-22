import time

from playwright.sync_api import Page, expect, Playwright

'''
def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)  #False ver el navegador
    context = browser.new_context() # do some operations  login  ->  can open multiple browsers and perform all the operations
    page = context.new_page()
    page.goto("https://www.google.com")
    print("test longcut")

#page  chromium headless mode 1 single context (implemented)
def test_playwrightShortCut(page:Page):
    page.goto("https://rahulshettyacademy.com/")
    print("test shortcut")
'''
def test_chrome(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2") #correcta
    #page.get_by_label("Password:").fill("Learnin") #incorrecta
    page.get_by_role("combobox").select_option("teach")  #combox
    page.get_by_role("link", name="terms and conditions").click() #links
    #checkbox ->  --#terms    class -> .text-info   tagName
    #page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click() #button
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    #expect(page.get_by_text("ProtoCommerce")).to_be_visible()
    time.sleep(10)

def test_firefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")  # correcta
    # page.get_by_label("Password:").fill("Learnin") #incorrecta
    page.get_by_role("combobox").select_option("teach")  # combox
    page.get_by_role("link", name="terms and conditions").click()  # links
    # checkbox ->  --#terms    class -> .text-info   tagName
    # page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()  # button
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    # expect(page.get_by_text("ProtoCommerce")).to_be_visible()
    time.sleep(10)

#need to asociate edit box  <label> Password <input type="password" /> <label/>

#https://rahulshettyacademy.com/angularpractice/shop