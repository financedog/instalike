#各モジュールを構成（なければcmdでpip install *** でインストール）
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
from time import sleep
import pyautogui

# herokuのchromedriverのPATHを指定
driver_path = '/app/.chromedriver/bin/chromedriver'
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options, executable_path=driver_path)




#instagramにアクセス
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)
sleep(1)
 #ログインID・PWを入力
elem_search_word = driver.find_element_by_name("username")
elem_search_word.send_keys("financedog")
sleep(1)
password = driver.find_element_by_name('password')
password.send_keys("yasu0119")
sleep(1)
password.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
sleep(10)
 #２段階認証の保存を選択
elem_search_word = driver.find_element_by_css_selector("button.sqdOP").click()
driver.implicitly_wait(5)
sleep(3)
 #ポップアップの後でを選択
elem_search_word = driver.find_element_by_css_selector("button.aOOlW").click()
driver.implicitly_wait(2)
sleep(1)
 #検索窓をアドレスバーに直接入力
driver.get("https://www.instagram.com/explore/tags/ポイ活/")
driver.implicitly_wait(6)
sleep(2)
 #Endkeyを押してスクロール、最大いいね数を増やす(１スクロールで20件表示を増やす)
pyautogui.hotkey('End')
driver.implicitly_wait(10)
sleep(6)

pyautogui.hotkey('End')
driver.implicitly_wait(10)
sleep(6)

pyautogui.hotkey('End')
driver.implicitly_wait(10)
sleep(6)

pyautogui.hotkey('End')
driver.implicitly_wait(10)
sleep(6)

pyautogui.hotkey('End')
driver.implicitly_wait(10)
sleep(6)

pyautogui.hotkey('End')
driver.implicitly_wait(10)
sleep(6)


driver.find_element_by_xpath("//article/div[1]/div[1]/div[1]/div[1]/div[1]/a").click()
sleep(1) #エラーになるまでいいねしつづける
likecount = 0
while (likecount < 70):
  try:
      #いいね判定
      sleep(1)
      driver.find_element_by_css_selector("[aria-label=「いいね！」を取り消す]")
      sleep(1)
      #いいねされていたらパス
      print("いいね済み、パス")
      driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
      sleep(1)
  except:
      #いいねする
      driver.find_element_by_css_selector("span.fr66n").click()
      likecount += 1
      sleep(1)
      print(likecount)
      print("いいね！")
      driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
      sleep(1)
      pass
print(likecount)
print("いいねしました！")
