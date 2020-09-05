#各モジュールを構成（なければcmdでpip install *** でインストール）
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
from time import sleep
import bs4
import random

driver_path = '/app/.chromedriver/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
#※headlessにしている
driver = webdriver.Chrome(options=options, executable_path=driver_path)

#instagramにアクセス
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)
sleep(1)
print("インスタグラムにアクセスしました")
 #ログインID・PWを入力
elem_search_word = driver.find_element_by_name("username")
elem_search_word.send_keys("financedog")
sleep(1)
print("ユーザーIDを入力しました")
password = driver.find_element_by_name('password')
password.send_keys("yasu01")
sleep(1)
print("ユーザーPWを入力しました")
password.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
sleep(10)
print("２段階認証に入ります")

 #２段階認証の保存を選択
elem_search_word = driver.find_element_by_css_selector("button.sqdOP").click()
driver.implicitly_wait(5)
sleep(5)



"""
1投稿目のインフルエンサーへ
""" #すきなインフルエンサーのURLを●●●にコピペします。

URL01 = ("https://www.instagram.com/ringo_56565/")
URL02 = ("●●●")
URL03 = ("●●●")
 #すきなインフルエンサーへのアクセス
driver.get(URL01)
driver.implicitly_wait(6)
sleep(1) #インフルエンサーへのアクセスプロセスを定義
def crowl():

   driver.find_elements_by_css_selector("li.Y8-fY")[1].click()
   sleep(3)
   li = driver.find_element_by_css_selector("div.isgrP")
   # 自動スクロール
   for i in range(30):
       driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", li)
       time.sleep(random.randint(500,1000)/1000)
   page_url = driver.page_source
   soup = bs4.BeautifulSoup(page_url,"lxml")
   elm = soup.find_all("a", {"class": "FPmhX notranslate _0imsa"})
   # フォロワーリスト化
   follower = []
   for e in elm:
       follower.append(e.text)
   list(set(follower))
   # フォロワー名表示
   print("リスト化したフォロワーを全表示します")
   list(set(follower))
   print(follower)
   sleep(3)
   # クローリング開始　100人のフォロワーにアクセス、いいねを押す
   for i in range(100):
       driver.get("https://www.instagram.com/" +str((*random.sample(follower,1))) + "/")
       sleep(2)
       try:
           #始めの記事をクリック
           driver.find_element_by_class_name("_9AhH0").click()
           sleep(1)
           #同じ人に3いいねをつける 判定をしていいね済みが３ついていると次の人へ遷移
           likecount = 0
           alreadycount = 0
           while (likecount < 3):
               try:
                   #いいね判定
                   driver.find_element_by_css_selector("[aria-label=「いいね！」を取り消す]")
                   sleep(2)
                   #いいねされていたらパス
                   print("いいね済み、パス")
                   alreadycount += 1
                   driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
                   sleep(1)
                   if alreadycount == 3:
                       break                   
               except:
                   #いいねする
                   try:
                      driver.find_element_by_xpath("/html/body/div[*]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
                      likecount += 1
                      sleep(1)
                      print(likecount)
                      print("いいね！")
                      driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
                      sleep(1)
                      if likecount == 3:
                       break
                   except:
                      driver.find_element_by_css_selector("[aria-label=いいね！]").click()
                      likecount += 1
                      sleep(1)
                      print(likecount)
                      print("いいね！")
                      driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
                      sleep(1)
                      if likecount == 3:
                       break
       except:
           pass
 #定義したクローリング関数を施行
           
crowl()


print("クローリング終了します")
driver.close()
