from playwright.sync_api import Page, expect
import re

def test_playwright_site_title(page):
    page.goto("https://playwright.dev")
    expect(page).to_have_title(re.compile("Playwright"))
