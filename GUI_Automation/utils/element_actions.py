import time

def verify_text(page, expected_text):
    body = (page.text_content("body") or "").lower()
    assert expected_text.lower() in body, f"❌ '{expected_text}' not found on page."
    print(f"✅ Verified text: '{expected_text}'")

def click_radio(page, name="Yes"):
    radio = page.get_by_role("radio", name=name)
    radio.scroll_into_view_if_needed()
    time.sleep(0.2)
    radio.click(force=True)
    print(f"✅ Clicked radio button: {name}")
