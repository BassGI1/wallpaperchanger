from requests import get
from ctypes import windll
from os import path, getcwd, remove
from playwright.sync_api import sync_playwright

URI = "https://apod.nasa.gov/apod/astropix.html"
JAVASCRIPT = """() => document.getElementsByTagName(\"IMG\")[0].src"""

def get_image_uri():
    with sync_playwright() as pl:
        browser = pl.chromium.launch()
        page = browser.new_page()
        page.goto(URI)
        return page.evaluate(JAVASCRIPT)


image = get(get_image_uri()).content
imagePath = path.join(getcwd(), "wallpaper.png")
with open("wallpaper.png", "wb") as file:
    file.write(image)

windll.user32.SystemParametersInfoW(20, 0, imagePath, 0)
remove(imagePath)