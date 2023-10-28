import re
import requests
import safaribooks
import playwright
import time
from playwright.sync_api import Playwright, sync_playwright, expect

"""
# 估计是有反爬虫，自动注册点击按钮不成功。
pip install playwright
"""
REGISTER_URL = safaribooks.SAFARI_BASE_URL + "/register/"
CHECK_EMAIL = safaribooks.SAFARI_BASE_URL + "/check-email-availability/"
CHECK_PWD = safaribooks.SAFARI_BASE_URL + "/check-password/"


trial_url = "https://www.oreilly.com/start-trial/"


FIRST_NAME = "Safari"
SECOND_NAME = "Download"


def register(email, password):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False,
                                             slow_mo=500, # wait .5s each
                                             proxy={
                                                 'server': "127.0.0.1:7890",
                                             },

                                             )
        context = browser.new_context()
        print("Registering %s / %s" % (email, password))
        page = context.new_page()
        page.goto("https://www.oreilly.com/start-trial/")
        page.get_by_test_id("userInfo-firstName").click()
        page.get_by_test_id("userInfo-firstName").fill("Ohayo")
        page.get_by_test_id("userInfo-lastName").click()
        page.get_by_test_id("userInfo-lastName").fill("Liu")
        page.get_by_test_id("userInfo-email").click()
        page.get_by_test_id("userInfo-email").fill(email)
        page.get_by_text("Create a password").click()
        page.get_by_test_id("userInfo-password").fill(password)
        page.get_by_label("Country:").select_option("CN")
        page.get_by_label("Referrer:").select_option("television-ad")

        page.get_by_test_id("submitButton").click()
        page.get_by_test_id("submitButton").dblclick()

        time.sleep(50)
        input("")
        # ---------------------
        # context.close()
        # browser.close()



if __name__ == "__main__":
    register("admin@example", "x")