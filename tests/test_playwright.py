from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    """Test Google search"""
    page.goto("https://www.google.com")
    page.get_by_role("button", name="Accept all").click() if page.get_by_role("button", name="Accept all").is_visible() else None
    
    search_box = page.get_by_role("combobox", name="Search")
    search_box.fill("Playwright Python")
    search_box.press("Enter")
    
    expect(page).to_have_title(lambda title: "Playwright Python" in title)

def test_example_com(page: Page):
    """Test example.com"""
    page.goto("https://example.com")
    expect(page.locator("h1")).to_have_text("Example Domain")
