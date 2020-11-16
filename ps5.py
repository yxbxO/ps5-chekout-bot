from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import user_info

'''

it's in very early stages. so far there arent any error checking in the code. if internet gets interrupted
or website takes a little longer to load the bot will mess up. oh and not to mention the ever loved captchas

only goes as far as to reviewing the order

'''

driver = webdriver.Chrome()

#goes to signin page and logsin
def signin(k):
    login_url = 'https://www.walmart.com/account/login?ref=domain'
    driver.get(login_url)
    try:
        usr = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
        )
        usr.send_keys(k['username'])
        print('username entry success')
    except:
        driver.quit()
    
    try:
        psswrd = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        psswrd.send_keys(k['password'])
        print('password entry success')
    except:
        driver.quit()

    try:
        login = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sign-in-form"]/button[1]'))
        )
        login.click()
        print('sign in success')
    except:
        driver.quit()

#checks if ps5 is out of stock and refreshs until it is not
def check_if_in_stock():
    time.sleep(1)
    #used this link instead of the ps5 for testing purposes
    driver.get('https://www.walmart.com/ip/TSV-PS4-Controller-Dual-Shock-Skin-Grip-Anti-slip-Silicone-Cover-Protector-Case-for-Sony-PS4-PS4-Slim-PS4-Pro-Controller-8-Thumb-Grips/304160322')
    #driver.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942')   
    base_url = ('https://www.walmart.com/ip/TSV-PS4-Controller-Dual-Shock-Skin-Grip-Anti-slip-Silicone-Cover-Protector-Case-for-Sony-PS4-PS4-Slim-PS4-Pro-Controller-8-Thumb-Grips/304160322')
    #base_url = ('https://www.walmart.com/ip/PlayStation-5-Console/363472942')
    session = HTMLSession()
    r = session.get(base_url)
    yo = r.html.find('link[href="//schema.org/OutOfStock"]', first=True)
    while yo != None:
        driver.refresh()
        time.sleep(1)
        print('Out Of Stock')
    print('In Stock!')

#this function needs a lot of work expecially lots of error handling. it looks for elements on the web and clicks on them
def checkout(k):
    try:
        #200 secs for time if captcha pops up
        addcart = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]'))
        )
        addcart.click()
        print('add to cart success')
    except:
        print('unsuccessful')
        driver.quit()

    try:
        cart = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]/span'))
        )
        cart.click()
        print('cart page success')
    except:
        driver.quit()
    
    try:
        d_date = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/span'))
        )
        d_date.click()
        print('delivery date success')
    except:
        driver.quit()

    try:
        addr = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button/span'))
        )
        time.sleep(1)
        addr.click()
        print('address confirm success')
    except:
        driver.quit()

    try:
        cvs = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cvv-confirm"]'))
        )
        cvs.send_keys(k['cvs'])
        print('cvs entry success')
    except:
        driver.quit()

    try:
        review_ord = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button/span/span'))
        )
        time.sleep(1)
        review_ord.click()
        print('order review success')
    except:
        driver.quit()

signin(user_info)
check_if_in_stock()
checkout(user_info)
time.sleep(5)
driver.close()