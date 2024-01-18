from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_sale():
    game_name = input("Name of the game: ")

    driver = webdriver.Chrome()

    driver.get('https://steamdb.info/sales/')

    search_box = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
    search_box.send_keys(game_name)

    wait = WebDriverWait(driver, 10)
    game = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, game_name)))

    try:
        sale_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#DataTables_Table_0 > tbody > tr > td:nth-child(5)'))).text
    except:
        sale_price = "Not found"

    try:
        sale_percentage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#DataTables_Table_0 > tbody > tr > td.price-discount'))).text
    except:
        sale_percentage = "Not found"

    print(game_name + " is on sale with a " + sale_percentage + " discount, which totals to " + sale_price +'!')

    driver.quit()

check_sale()
