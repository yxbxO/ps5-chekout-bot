from selenium import webdriver
from requests_html import HTMLSession, AsyncHTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import user_info

driver = webdriver.Chrome()

#goes to signin page and enters login info
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
def check_if_in_stock(k):
    time.sleep(1)
    #used this link instead of the ps5 for testing purposes
    base_url = (k['URL'])
    driver.get(base_url)   
    session = HTMLSession()
    r = session.get(base_url)
    yo = r.html.find('.prod-blitz-copy-message', first=True)
    while yo != None:
        driver.refresh()
        time.sleep(2)  
        session = HTMLSession()
        r = session.get(base_url)
        yo = r.html.find('.prod-blitz-copy-message', first=True)
        print(yo, ' = Out Of Stock')
    print('In Stock!')

#this function needs a lot of work expecially lots of error handling. it looks for elements on the web and clicks on them
def checkout(k):
    try:
        #200 secs for time if captcha pops up
        amnt = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[2]/select'))
        )
        addcart = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]'))
        )
        amnt.send_keys(k['amount'])
        addcart.click()
        print('added to cart')
    except:
        print('unsuccessful')
        driver.refresh()

    try:
        cart = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]/span'))
        )
        cart.click()
        print('went to cart page successfully')
    except:
        driver.quit()
    
    #200sec wait time in case of captcha
    try:
        d_date = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/span'))
        )
        d_date.click()
        print('delivery date confirmed')
    except:
        driver.quit()

    #200sec wait time in case of captcha
    try:
        addr = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button/span'))
        )
        time.sleep(1)
        addr.click()
        print('address confirm success')
    except:
        driver.quit()

    #200sec wait time in case of captcha
    try:
        cvs = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cvv-confirm"]'))
        )
        cvs.send_keys(k['cvs'])
        print('cvs entry success')
    except:
        driver.quit()

    #200sec wait time in case of captcha
    try:
        review_ord = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button/span/span'))
        )
        #time.sleep(1)
        review_ord.click()
        print('order review success')
    except:
        driver.quit()

    try:
        place_ord = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button/span'))
        )
        place_ord.click()
        print('order placed successfully')
    except:
        driver.quit()

if __name__ == "__main__":
    signin(user_info)
    check_if_in_stock(user_info)
    checkout(user_info)
    time.sleep(5)
    driver.close()