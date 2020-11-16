from selenium import webdriver
from requests_html import HTMLSession, AsyncHTMLSession
from selenium.webdriver.common.keys import Keys
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
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(k['username'])
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(k['password'])
    driver.find_element_by_xpath('//*[@id="sign-in-form"]/button[1]').click()

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
    driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="cvv-confirm"]').send_keys(k['cvs'])
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button/span/span').click()


signin(user_info)
check_if_in_stock()
checkout(user_info)