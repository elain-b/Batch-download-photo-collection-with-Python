import os
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

# アルバムフォルダ作成
os.mkdir("/Users/YOUR PC NAME/Downloads/album")

# 1個目のドライバーを立ち上げる
driver = webdriver.Chrome('/Users/YOUR PC NAME/Downloads/chromedriver')
driver.implicitly_wait(10)

# ログイン1回目ブラウザ立ち上げ
driver.get('https://photozou.jp/basic/login')
driver.implicitly_wait(10)

# ログイン
element = driver.find_element_by_id("email")
element.click()
driver.implicitly_wait(10)
sleep(0.5)
pyperclip.copy('YOUR MAIL ADRESS')
pyautogui.hotkey("command", "v")
sleep(0.5)
element = driver.find_element_by_id("password")
element.click()
driver.implicitly_wait(10)
pyperclip.copy('YOUR PASSWORD')
pyautogui.hotkey("command", "v")
sleep(1)
element = driver.find_element_by_class_name("btn_submit")
element.click()
driver.implicitly_wait(10)

# アルバム移動
element = driver.find_element_by_link_text("わたしの写真")
element.click()

# アルバムページ取得
driver.get('http://photozou.jp/photo/top/1680833')
driver.implicitly_wait(2)

# アルバム名取得
element = driver.find_element_by_id("photo_filter_album_id")
select = Select(element)
selectop = select.options
del selectop[0]
driver.implicitly_wait(10)

# 全アルバム名をリスト配列へ代入とフォルダ作成
a = []
for j in range(len(selectop)):
    a.append(selectop[j].text)
    albumpath = "/Users/YOUR PC NAME/Downloads/album/" + a[j]
    os.mkdir(albumpath)
    print("Index:", j, "  Name:", a[j])
driver.close()
sleep(1)

# 全ての画像をアルバムごとに保存
# for i in range(len(selectop)):
for i in range(39,40):

    # 2個目のドライバーを立ち上げる
    chop = webdriver.ChromeOptions()
    albumpath = "/Users/YOUR PC NAME/Downloads/album/" + a[i]
    prefs = {"download.default_directory": albumpath}
    chop.add_experimental_option("prefs", prefs)
    # chop.add_argument('--ignore-certificate-errors')
    chop.add_argument('-–disable-dev-shm-usage')
    chop.add_argument('--disable-extensions')
    chromedrv = '/Users/YOUR PC NAME/Downloads/chromedriver'
    driver2 = webdriver.Chrome(executable_path=chromedrv, options=chop)
    driver2.set_page_load_timeout(15)
    driver2.implicitly_wait(10)

    # ログイン2回目ブラウザ立ち上げ
    driver2.get('https://photozou.jp/basic/login')
    driver2.implicitly_wait(10)

    # 2回目のログイン
    element = driver2.find_element_by_id("email")
    element.click()
    driver2.implicitly_wait(10)
    sleep(0.5)
    pyperclip.copy('YOUR MAIL ADRESS')
    pyautogui.hotkey("command", "v")
    sleep(0.5)
    element = driver2.find_element_by_id("password")
    element.click()
    driver2.implicitly_wait(10)
    pyperclip.copy('YOUR PASSWORD')
    pyautogui.hotkey("command", "v")
    sleep(1)
    driver2.implicitly_wait(15)
    element = driver2.find_element_by_class_name("btn_submit")
    element.click()

    # アルバム移動
    driver2.implicitly_wait(15)
    element = driver2.find_element_by_link_text("わたしの写真")
    element.click()
    sleep(1)

    # アルバムの切り替え
    driver2.implicitly_wait(10)
    driver2.get('http://photozou.jp/photo/top/1680833')
    driver2.implicitly_wait(15)
    element = driver2.find_element_by_id("photo_filter_album_id")
    driver2.implicitly_wait(10)
    select = Select(element)
    select.select_by_index(i+1)
    driver2.implicitly_wait(15)

    # 画像の保存
    while True:
        try:
            element = driver2.find_elements_by_link_text("保存")
            driver2.implicitly_wait(5)
            for i in element:
                i.click()
                driver2.implicitly_wait(10)
                sleep(1)
            nextpage = driver2.find_element_by_link_text("次へ")
            nextpage.click()
            driver2.implicitly_wait(15)
            sleep(0.5)
        except:
            break

    # ブラウザを閉じる
    sleep(2)
    driver2.close()
print('終了しました。')