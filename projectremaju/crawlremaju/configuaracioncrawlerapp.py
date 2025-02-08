from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from playwright.async_api import Page, BrowserContext

# 1) Configure the browser
browser_config = BrowserConfig(
    headless=True,
    verbose=True
)

# 2) Configure the crawler run
crawler_run_config = CrawlerRunConfig(
    js_code="window.scrollTo(0, document.body.scrollHeight);",
    wait_for="body",
    cache_mode=CacheMode.BYPASS
)

# 3) Create the crawler instance
crawler = AsyncWebCrawler(config=browser_config)
    #
    # Define Hook Functions
    #
async def on_browser_created(browser, **kwargs):
    # Called once the browser instance is created (but no pages or contexts yet)
    print("[HOOK] on_browser_created - Browser created successfully!")
    # Typically, do minimal setup here if needed
    return browser
async def on_page_context_created(page: Page, context: BrowserContext, **kwargs):
    # Called right after a new page + context are created (ideal for auth or route config).
    print("[HOOK] on_page_context_created - Setting up page & context.")
    await page.fill("input[name='username']", "admin@example.com")
    await page.fill("input[name='password']", "password")
    await page.click("button[type='submit']")
    await page.wait_for_selector("#main-content")
    

    # Example 1: Route filtering (e.g., block images)
    #async def route_filter(route):
    #    if route.request.resource_type == "image":
    #        print(f"[HOOK] Blocking image request: {route.request.url}")
    #        await route.abort()
    #    else:
    #        await route.continue_()
    #await context.route("**", route_filter)
    
    # Example 2: (Optional) Simulate a login scenario
    # (We do NOT create or close pages here, just do quick steps if needed)
    # e.g., await page.goto("https://example.com/login")
    # e.g., await page.fill("input[name='username']", "testuser")
    # e.g., await page.fill("input[name='password']", "password123")
    # e.g., await page.click("button[type='submit']")
    # e.g., await page.wait_for_selector("#welcome")
    # e.g., await context.add_cookies([...])
    # Then continue
    # Example 3: Adjust the viewport
    await page.set_viewport_size({"width": 1080, "height": 600})
    return page