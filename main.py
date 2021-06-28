def main():

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager


    # Chrome起動オプション
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


    # 指定サイトURL
    url = "https://www.instagram.com/accounts/login/"


    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(5)
    driver.get(url)


    # アカウント情報
    id = "financedog"
    ps = "yasu01"


    driver.find_element_by_css_selector("input[name='username']").send_keys(id)
    driver.find_element_by_css_selector("input[name='password']").send_keys(ps)
    driver.find_element_by_css_selector("button[type='submit']").click()


    print("ログイン完了")
    driver.quit()

if __name__ == '__main__':
    main()
