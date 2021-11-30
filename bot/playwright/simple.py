# https://playwright.dev/python/docs/intro/

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    page.screenshot(path="example.png")
    browser.close()
