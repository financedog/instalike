def main():

    from selenium import webdriver
    import random
    from time import sleep
    # Chrome起動オプション

    driver_path = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    #driverに設定 ※optionsを指定しないとheadlessにならないので注意
    driver = webdriver.Chrome(options=options, executable_path=driver_path)

    # ログインページURL
    url = "https://www.instagram.com/accounts/login/"

    # アカウント情報
    id = "financedog"

    ps = "yasu01"

    tag ="ポイ活"

    count="70"

    # ブラウザ起動
    driver.get(url)
    driver.implicitly_wait(15)
    sleep(3)

    print("ログインページにアクセス")


    # ログイン処理
    user = driver.find_element_by_css_selector("input[name='username']")
    user.send_keys(id)
    print("ログインIDを入力")
    sleep(2)

    password = driver.find_element_by_css_selector("input[name='password']")
    password.send_keys(ps)
    print("PWを入力")
    sleep(2)

    #accept allをクリック
    try:
       driver.find_element_by_xpath("//button[text()='Accept All']").click()
       print("accept allをクリックしました")
    except:
        pass

    #ログインできない場合は正規にインスタにログインして、実行すること
    login = driver.find_element_by_css_selector("button[type='submit']")
    login.click()
    print("ログインしました")
    sleep(2)

    #２段階認証の保存を選択

    elem_search_word = driver.find_element_by_css_selector("button.sqdOP").click()
    driver.implicitly_wait(5)
    sleep(3)
    print("２段階認証をクリア")

    # 検索窓をアドレスバーに直接入力
    driver.get("https://www.instagram.com/explore/tags/" + (tag) + "/")
    sleep(2)
    print("タグ検索アクセス")

    driver.find_element_by_xpath("//article/div[1]/div[1]/div[1]/div[1]/div[1]/a").click()
    sleep(1)
    print("始めの投稿にアクセスしました")


    # エラーになるまでいいねしつづける
    likecount = 0
    while (likecount < int(count)):

        try:

            #いいねする
            driver.find_element_by_css_selector("span.fr66n").click()
            likecount += 1
            sleep(1)
            print(likecount)
            print("いいね！")
            driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
            sleep(1)
            pass



        except:
            #いいね判定
            sleep(1)
            driver.find_element_by_css_selector("[aria-label=「いいね！」を取り消す]")
            sleep(1)
            #いいねされていたらパス
            print("いいね済み、パス")
            driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
            sleep(1)


    print(likecount)
    print("いいねしました！")


    driver.quit()

if __name__ == '__main__':
    main()
