from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        page.goto("file:///app/index.html")

        # Wait for the table to be visible
        page.wait_for_selector("table")

        # Check for presence of new sentences
        assert page.get_by_text("Alice purchased a Persian Rug while visiting Tabriz on March 15, 2025.").is_visible()
        assert page.get_by_text("On September 2, 2023, Bob bought a Venetian Mask in Venice.").is_visible()

        # Check that old labels are gone
        # We expect "Category:" to NOT be visible in the visible text
        # (It might be in the source code if I missed something, but it shouldn't be rendered)
        try:
            assert not page.get_by_text("Category:").is_visible()
        except Exception:
            # get_by_text might throw if not found, or return hidden element.
            # If it returns a handle, is_visible() returns bool.
            # If it doesn't find it, it waits until timeout.
            # So checking count is safer for negative assertion.
            pass

        count = page.get_by_text("Category:").count()
        assert count == 0, f"Found 'Category:' {count} times"

        # Take screenshot
        page.screenshot(path="verification/index_screenshot.png", full_page=True)

        print("Verification successful. Screenshot saved to verification/index_screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
