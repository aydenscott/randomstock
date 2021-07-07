from selenium import webdriver
import pyautogui, time

driver = webdriver.Chrome()
source = r"https://raybb.github.io/random-stock-picker/"
driver.get(source)
driver.maximize_window()

# Retrieve tickers
tickers = []
count = 0
while count != 5:
    ticker = driver.find_element_by_id("ticker").text
    tickers.append(ticker)
    count += 1
    driver.refresh()

# Open google tabs for tickers
for i in tickers:
    pyautogui.hotkey("ctrl", "t")
    pyautogui.typewrite(str(i) + " stock")
    pyautogui.hotkey("enter")
    time.sleep(0.5)

