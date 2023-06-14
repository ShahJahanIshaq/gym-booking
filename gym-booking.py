from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from plyer import notification
from datetime import datetime

GYM = "B-ACTIVE"
REQUIRED_DATE = "Friday"
REQUIRED_TIME = "1700"

available = False

now = datetime.now()
current_time = now.strftime("%H%M")

driver = webdriver.Chrome()

booking_url = "https://fcbooking.cse.hku.hk/Form/SignUp"

while not available and int(current_time) < 2030:
    
    driver.get(booking_url)

    center = Select(driver.find_element(By.ID, "CenterID"))
    center.select_by_index(2)
    sleep(1)
    date = Select(driver.find_element(By.ID, "DateList"))
    for idx, opt in enumerate(date.options):
        if REQUIRED_DATE in opt.text:
            date.select_by_index(idx)
    sleep(1)
    time = Select(driver.find_element(By.ID, "SessionTime"))
    for idx, opt in enumerate(time.options):
        if REQUIRED_TIME in opt.text:
            if "Full" not in opt.text:
                available = True
            else:
                available = False
            break

    if available:
        print(f"[URGENT] Booking Available! Current Time: {datetime.now().strftime('%H:%M:%S')}")
        notification.notify(
            title = "GYM BOOKING AVAILABLE",
            message = f"{REQUIRED_DATE} at {REQUIRED_TIME} is available at {GYM}",
            app_icon = "gym-notif-icon.ico",
            timeout = 10
        )
        break
    sleep(3)