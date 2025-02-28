from selenium import webdriver
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

        psswrd = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        psswrd.send_keys(k['password'])
        print('password entry success')

        login = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sign-in-form"]/button[1]'))
        )
        login.click()
        print('sign in success')
    except:
        driver.quit()

def error_checking(k, cur_url, *arg):
    while cur_url != k['URL'] or arg:
        print('complete the captcha please')
        time.sleep(2)
        cur_url = driver.current_url
        if cur_url == k['URL'] or arg:
            break


#checks if ps5 is out of stock and refreshs until it is not
def check_if_in_stock(k):
    time.sleep(1)
    base_url = (k['URL'])
    driver.get(base_url) 
    while(1):
        try:
        #200 secs for time if captcha pops up
            amnt = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[2]/select'))
            )
            addcart = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]'))
            )
            print
            amnt.send_keys(k['amount'])
            addcart.click()
            print('added to cart')
            break
        except:
            print('OUT OF STOCK')
            cur_url = driver.current_url
            print(cur_url)
            error_checking(user_info, cur_url)
            print('refreshing...\n')
            driver.refresh()


#this function needs a lot of work expecially lots of error handling. it looks for elements on the web and clicks on them
def checkout(k):
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