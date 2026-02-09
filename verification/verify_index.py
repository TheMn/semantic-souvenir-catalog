from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html file
        page.goto(f"file://{os.getcwd()}/index.html")

        # Wait for the table to be visible
        page.wait_for_selector("table")

        # Take a screenshot of the entire page
        page.screenshot(path="verification/index_screenshot.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
