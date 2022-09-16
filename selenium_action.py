from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from db import Database
from cfg import get_phone_number
db = Database('wb_db.db')




def execute():
    url = 'https://www.wildberries.ru/security/login'
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\Данил\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
    driver = webdriver.Chrome(options=options) #WebDriver
    #Authorization
    # driver.get(url=url)
    # inp_form = driver.find_element_by_class_name('input-item')
    # inp_form.clear()
    # inp_form.click()
    # time.sleep(2)
    # inp_form.send_keys(get_phone_number())
    # time.sleep(2)
    # button = driver.find_element_by_id('requestCode')
    # button.click()
    # time.sleep(2)
    # code = input("Введите код подтверждения: ")
    # inp_form2 = driver.find_element_by_xpath('//*[@id="spaAuthForm"]/div/div[3]/div/input')
    # inp_form2.send_keys(code)
    # time.sleep(2)
    #Main process
    driver.get('https://www.wildberries.ru')
    driver.set_window_size(700, 1000)
    time.sleep(2)
    inp_form3 = driver.find_element_by_class_name('nav-element__search')
    time.sleep(2)
    inp_form3.click()
    time.sleep(2)
    inp_form3_1 = driver.find_element_by_id('mobileSearchInput')
    time.sleep(2)
    inp_form3_1.click()
    time.sleep(2)
    inp_form3_1.send_keys(db.get_articul())
    time.sleep(2)
    inp_form3_1.send_keys(Keys.ENTER)
    time.sleep(2)
    #BUY
    buy_butt = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/div[8]/div[1]/div/button[1]')
    time.sleep(2)
    buy_butt.click()
    time.sleep(2)
    try:
        punkt_butt = driver.find_element_by_class_name('j-btn-choose-address')
    except:
        punkt_butt = driver.find_element_by_class_name('basket-section__btn-change')
    time.sleep(2)
    punkt_butt.click()
    time.sleep(2)
    punkt_butt2 = driver.find_element_by_class_name('popup__btn-base')
    time.sleep(2)
    punkt_butt2.click()
    time.sleep(2)
    punkt_input = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/ymaps/ymaps/ymaps/ymaps[4]/ymaps[1]/ymaps[1]/ymaps/ymaps[1]/ymaps/ymaps/ymaps/ymaps/ymaps[1]/ymaps/ymaps[1]/ymaps[1]/input')
    time.sleep(2)
    punkt_input.click()
    punkt_input.send_keys(db.get_punkt())
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    punkt_input1 = driver.find_element_by_class_name('ymaps-2-1-79-search__suggest-item')
    time.sleep(2)
    punkt_input1.click()
    time.sleep(2)
    punkt_s = driver.find_element_by_class_name('address-item')
    time.sleep(2)
    punkt_s.click()
    time.sleep(2)
    choose_button = driver.find_element_by_class_name('j-btn-select-poo')
    time.sleep(2)
    choose_button.click()
    time.sleep(2)
    close = driver.find_element_by_class_name('popup__btn-main')
    time.sleep(2)
    close.click()
    time.sleep(2)
    buy = driver.find_element_by_class_name('b-btn-do-order')
    time.sleep(2)
    buy.click()
    driver.quit()


def feedback(feed_text):
    driver = webdriver.Chrome()
    driver.get('https://www.wildberries.ru/security/login')
    inp_form = driver.find_element_by_class_name('input-item')
    inp_form.clear()
    inp_form.click()
    time.sleep(2)
    inp_form.send_keys(get_phone_number())
    time.sleep(2)
    button = driver.find_element_by_id('requestCode')
    button.click()
    time.sleep(2)
    code = input("Введите код подтверждения: ")
    inp_form2 = driver.find_element_by_xpath('//*[@id="spaAuthForm"]/div/div[3]/div/input')
    inp_form2.send_keys(code)
    time.sleep(2)
    driver.get('https://www.wildberries.ru/lk/myorders/archive')
    time.sleep(2)
    driver.set_window_size(1920, 1080)
    time.sleep(2)
    scrollbar = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[1]/label/span')
    time.sleep(2)
    scrollbar.click()
    time.sleep(2)
    scrollbar_ready = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[1]/div/label[2]/span')
    time.sleep(2)
    scrollbar_ready.click()
    time.sleep(2)
    feed = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div[2]/div/ul/li[1]/div/div[2]/div[2]/div/button')
    time.sleep(2)
    feed.click()
    time.sleep(2)
    feed_form = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/textarea')
    time.sleep(2)
    feed_form.click()
    time.sleep(2)
    feed_form.send_keys(feed_text)
    time.sleep(2)
    final_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[4]/button[2]')
    time.sleep(2)
    final_button.click()






if __name__ == "__main__":
    execute()