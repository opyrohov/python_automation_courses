"""Example 6: Async API for Multiple Pages

Demonstrates the same concepts using async/await syntax.
Async API is useful for:
- Better performance with parallel operations
- Integration with async frameworks (FastAPI, aiohttp)
- More control over concurrent operations
"""
import asyncio
from playwright.async_api import async_playwright, expect


async def basic_multi_page():
    """Basic example of managing multiple pages asynchronously."""
    print("=== Async Multi-Page Demo ===\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()

        # Create multiple pages
        print("1. Creating pages asynchronously...")
        page1 = await context.new_page()
        page2 = await context.new_page()

        # Navigate both pages in parallel (faster!)
        print("2. Navigating pages in PARALLEL...")
        await asyncio.gather(
            page1.goto("https://example.com"),
            page2.goto("https://the-internet.herokuapp.com/")
        )
        print(f"   Page 1: {page1.url}")
        print(f"   Page 2: {page2.url}")

        # Get titles in parallel
        print("\n3. Getting titles in parallel...")
        titles = await asyncio.gather(
            page1.title(),
            page2.title()
        )
        print(f"   Titles: {titles}")

        await browser.close()
        print("\n   Done!")


async def async_popup_handling():
    """Handle popups with async API."""
    print("\n=== Async Popup Handling ===\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://the-internet.herokuapp.com/windows")

        # Handle popup with async context manager
        print("1. Capturing popup asynchronously...")
        async with page.expect_popup() as popup_info:
            await page.locator("a[href='/windows/new']").click()

        popup = await popup_info.value
        await popup.wait_for_load_state()

        print(f"   Popup URL: {popup.url}")
        print(f"   Popup title: {await popup.title()}")

        await popup.close()
        await browser.close()
        print("   Done!")


async def async_popup_with_timeout():
    """Handle popup with custom timeout."""
    print("\n=== Async Popup with Timeout ===\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://the-internet.herokuapp.com/windows")

        # expect_popup with timeout - wait up to 5 seconds
        print("1. Waiting for popup with 5 second timeout...")
        try:
            async with page.expect_popup(timeout=5000) as popup_info:
                await page.locator("a[href='/windows/new']").click()

            popup = await popup_info.value
            await popup.wait_for_load_state()
            print(f"   Popup captured: {popup.url}")
            await popup.close()

        except Exception as e:
            print(f"   Timeout or error: {e}")

        await browser.close()
        print("   Done!")


async def async_context_expect_page():
    """Use context.expect_page() to capture new pages."""
    print("\n=== Async context.expect_page() ===\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://the-internet.herokuapp.com/windows")

        # context.expect_page() captures ANY new page in context
        print("1. Using context.expect_page()...")
        async with context.expect_page() as new_page_info:
            await page.locator("a[href='/windows/new']").click()

        new_page = await new_page_info.value
        await new_page.wait_for_load_state()

        print(f"   New page URL: {new_page.url}")
        print(f"   Total pages in context: {len(context.pages)}")

        await new_page.close()
        await browser.close()
        print("   Done!")


async def async_multi_user_parallel():
    """Multi-user testing with parallel operations."""
    print("\n=== Async Multi-User (Parallel) ===\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=200)

        # Create contexts in parallel
        print("1. Creating isolated contexts...")
        ctx1, ctx2 = await asyncio.gather(
            browser.new_context(),
            browser.new_context()
        )

        # Create pages in parallel
        user1, user2 = await asyncio.gather(
            ctx1.new_page(),
            ctx2.new_page()
        )

        # Both users navigate to login in parallel
        print("2. Both users navigating to login page...")
        await asyncio.gather(
            user1.goto("https://the-internet.herokuapp.com/login"),
            user2.goto("https://the-internet.herokuapp.com/login")
        )

        # User 1 logs in
        print("3. User 1 logging in...")
        await user1.locator("#username").fill("tomsmith")
        await user1.locator("#password").fill("SuperSecretPassword!")
        await user1.locator("button[type='submit']").click()

        # Verify both users' states in parallel
        print("4. Verifying user states in parallel...")
        await asyncio.gather(
            expect(user1.locator(".flash.success")).to_be_visible(),
            expect(user2.locator("#username")).to_be_visible()
        )

        print("   User 1: Logged in (sees success message)")
        print("   User 2: Not logged in (sees login form)")
        print("   Contexts are properly isolated!")

        await browser.close()
        print("   Done!")


async def async_page_events():
    """Handle page events asynchronously."""
    print("\n=== Async Page Events ===\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context()

        pages_opened = []

        # Event handler for new pages
        def on_page(page):
            pages_opened.append(page)
            print(f"   EVENT: New page opened")

        context.on("page", on_page)

        print("1. Creating pages (events will fire)...")
        page1 = await context.new_page()
        page2 = await context.new_page()

        print(f"   Total pages tracked: {len(pages_opened)}")

        # Console event handling
        print("\n2. Console message handling...")
        console_msgs = []

        def on_console(msg):
            console_msgs.append(msg.text)
            print(f"   CONSOLE: {msg.text}")

        page1.on("console", on_console)

        await page1.goto("https://example.com")
        await page1.evaluate("console.log('Hello from async Playwright!')")

        print(f"   Total console messages: {len(console_msgs)}")

        await browser.close()
        print("   Done!")


async def main():
    """Run all async examples."""
    await basic_multi_page()
    await async_popup_handling()
    await async_popup_with_timeout()
    await async_context_expect_page()
    await async_multi_user_parallel()
    await async_page_events()

    print("\n" + "="*50)
    print("All async examples completed!")
    print("="*50)


if __name__ == "__main__":
    asyncio.run(main())
