from playwright.sync_api import sync_playwright
import time
import datetime as dt

now = dt.datetime.now()
today = f'{now.year}_{now.month}_{now.day}'

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto('https://battlepod.playdonut.com/')

time.sleep(3)

page.locator('.bp_id').fill('***')
time.sleep(0.5)
page.locator('.bp_pw').fill('***')
time.sleep(0.5)
page.get_by_role("button", name="로그인").click()
time.sleep(2)
page.screenshot(path=f'bp_{today}.png')

time.sleep(5)

page.close()
