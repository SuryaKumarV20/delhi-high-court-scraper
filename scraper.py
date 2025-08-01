from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def fetch_case_details(case_type, case_number, filing_year):
    try:
        print("[INFO] Fetching case info...")
        CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "chromedriver-win64", "chromedriver.exe")

        service = Service(CHROMEDRIVER_PATH)
        options = webdriver.ChromeOptions()
        
        # Headed mode for debugging
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=service, options=options)
        driver.set_page_load_timeout(30)

        print("[INFO] Opening site...")
        driver.get("https://delhihighcourt.nic.in/case.asp")

        wait = WebDriverWait(driver, 15)
        print("[INFO] Waiting for form fields...")
        wait.until(EC.presence_of_element_located((By.NAME, "ctype")))

        print("[INFO] Filling form...")
        Select(driver.find_element(By.NAME, "ctype")).select_by_visible_text(case_type)
        driver.find_element(By.NAME, "cnumber").send_keys(case_number)
        driver.find_element(By.NAME, "cyear").send_keys(filing_year)

        print("[INFO] Submitting...")
        driver.find_element(By.XPATH, "//input[@value='Submit']").click()

        time.sleep(3)
        html = driver.page_source
        print("[INFO] Done. Length of HTML:", len(html))

        return html

    except Exception as e:
        print("[ERROR] Exception occurred:", str(e))
        return f"❌ Error: {str(e)}"

    finally:
        try:
            driver.quit()
        except:
            pass
