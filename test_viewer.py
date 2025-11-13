#!/usr/bin/env python3
"""
Playwright test for Carmatz viewer
Tests that version label is visible and page loads correctly
"""

import asyncio
import subprocess
import time
from playwright.async_api import async_playwright

async def test_viewer():
    print("Starting HTTP server...")
    server = subprocess.Popen(
        ['python', '-m', 'http.server', '8080'],
        cwd='.',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Wait for server to start
    time.sleep(2)

    try:
        async with async_playwright() as p:
            print("Launching Chromium...")
            browser = await p.chromium.launch(headless=True)

            # Test desktop view
            print("\n=== Testing Desktop View ===")
            context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
            page = await context.new_page()

            print("Loading page...")
            await page.goto('http://localhost:8080/carmatz1.html')

            # Wait for model viewer to load
            print("Waiting for model-viewer...")
            await page.wait_for_selector('model-viewer', timeout=10000)

            # Check for version label
            print("Checking for version label...")
            version_label = await page.query_selector('.version-label')
            if version_label:
                version_text = await version_label.text_content()
                is_visible = await version_label.is_visible()
                print(f"[OK] Version label found: {version_text}")
                print(f"  Visible: {is_visible}")

                # Get position
                box = await version_label.bounding_box()
                if box:
                    print(f"  Position: left={box['x']}px, bottom={1080-box['y']-box['height']}px")
                else:
                    print("  WARNING: Version label has no bounding box!")
            else:
                print("[FAIL] Version label NOT found!")

            # Check for cache panel
            print("\nChecking for cache panel...")
            cache_panel = await page.query_selector('.cache-panel')
            if cache_panel:
                is_visible = await cache_panel.is_visible()
                print(f"[OK] Cache panel found")
                print(f"  Visible: {is_visible}")
            else:
                print("[FAIL] Cache panel NOT found!")

            # Check for location title
            print("\nChecking for location title...")
            location_title = await page.query_selector('.location-title')
            if location_title:
                title_text = await location_title.text_content()
                is_visible = await location_title.is_visible()
                print(f"[OK] Location title found: {title_text}")
                print(f"  Visible: {is_visible}")
            else:
                print("[FAIL] Location title NOT found!")

            # Take screenshot
            print("\nTaking screenshot...")
            await page.screenshot(path='test-desktop.png', full_page=True)
            print("[OK] Screenshot saved to test-desktop.png")

            await context.close()

            # Test mobile view
            print("\n=== Testing Mobile View ===")
            context = await browser.new_context(viewport={'width': 375, 'height': 812})
            page = await context.new_page()

            print("Loading page...")
            await page.goto('http://localhost:8080/carmatz1.html')

            # Wait for model viewer
            await page.wait_for_selector('model-viewer', timeout=10000)

            # Check version label on mobile
            print("Checking for version label on mobile...")
            version_label = await page.query_selector('.version-label')
            if version_label:
                is_visible = await version_label.is_visible()
                version_text = await version_label.text_content()
                print(f"[OK] Version label found: {version_text}")
                print(f"  Visible: {is_visible}")
            else:
                print("[FAIL] Version label NOT found!")

            # Take mobile screenshot
            print("\nTaking mobile screenshot...")
            await page.screenshot(path='test-mobile.png', full_page=True)
            print("[OK] Screenshot saved to test-mobile.png")

            await context.close()
            await browser.close()

            print("\n=== All Tests Complete ===")
            print("Check test-desktop.png and test-mobile.png for visual verification")

    finally:
        print("\nStopping HTTP server...")
        server.terminate()
        server.wait()

if __name__ == '__main__':
    asyncio.run(test_viewer())
