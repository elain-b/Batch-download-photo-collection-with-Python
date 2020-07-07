import os
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.support.select import Select

os.mkdir("/Users/taniteiko/Downloads/album")

driver = webdriver.Chrome('/Users/taniteiko/Downloads/chromedriver')
# 指定したURLのWebページへ遷移
driver.implicitly_wait(10)
driver.get('https://photozou.jp/basic/login')

# print(pyautogui.position())
path = "51830002.cj@gmail.com"
driver.implicitly_wait(10)
pyautogui.click(406, 507)
driver.implicitly_wait(10)
pyperclip.copy('51830002.cj@gmail.com')
pyautogui.hotkey("command","v")
driver.implicitly_wait(10)
pyautogui.click(404, 551)
pyautogui.typewrite("kureteyaru")
pyautogui.click(473, 645)
driver.implicitly_wait(10)
# pyautogui.click(882, 544)
# driver.find_element_by_xpath("/photo/top/1680833").click()
element = driver.find_element_by_link_text("わたしの写真")
element.click()

driver.get('http://photozou.jp/photo/top/1680833')
driver.implicitly_wait(2)
element = driver.find_element_by_id("photo_filter_album_id")
select = Select(element)
selectop = select.options
del selectop[0]
for i in range(len(selectop)):
    driver.get('http://photozou.jp/photo/top/1680833')
    driver.implicitly_wait(2)
    element = driver.find_element_by_id("photo_filter_album_id")
    select = Select(element)
    select.select_by_index(i+1)
    driver.implicitly_wait(2)
    selected = select.options
    driver.implicitly_wait(2)
    albumpath = "/Users/taniteiko/Downloads/album/" + selected[0].text
    os.mkdir(albumpath)

    # while True:
    #     try:
    #         element = driver.find_elements_by_link_text("保存")
    #         # for i in element:
    #         #     i.click()
    #         driver.implicitly_wait(10)
    #         nextpage = driver.find_element_by_link_text("次へ")
    #         nextpage.click()
    #     except:
    #         break
