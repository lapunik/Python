import time
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import webbrowser
import win32gui
import win32con
 
options = Options()
options.headless = True

url = "https://nesnezeno.eco/produkt/foodora-market-balicek-plzen/"

# vybereme prohlížeč a otevřeme webovou stránku 
driver = webdriver.Firefox(options=options)
driver.get(url)

# počkáme než se stránka spustí
wait = WebDriverWait(driver, 10) 

# odkliknutí cookies
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
button.click()

print("Program monitouje...\n")

while (True):   
    
    driver.refresh()
    element = driver.find_element(By.CSS_SELECTOR,'.stock-status')

    if(element.text ==  "Skladem"):
        print("Je to skladem, kupujeme!")
        driver.quit()
        webbrowser.open(url)    
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        winsound.PlaySound('alarm',0)
        break

    time.sleep(1)  # Počkejte sekundu před dalším načtením stránky

# otevři nesnezeno v edge