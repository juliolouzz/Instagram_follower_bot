from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

SIMILAR_ACCOUNT = ""  # name of the instagram you want to copy like "googleuk"
INSTAGRAM_USERNAME = ""  # your username
INSTAGRAM_PASSWORD = ""  # your password
SCROLL_DOWN = 5  # how many times you want to scroll down to load followers


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        cookies_1 = self.driver.find_element(By.CSS_SELECTOR, "div > button._a9--._a9_0")
        cookies_1.click()
        sleep(1)
        username_container = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_container.send_keys(INSTAGRAM_USERNAME)
        password_container = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_container.send_keys(INSTAGRAM_PASSWORD)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()
        sleep(6)
        save_info_btn = self.driver.find_element(By.CSS_SELECTOR, "div > button._acan._acap._acas._aj1-")
        save_info_btn.click()
        sleep(2)
        turn_off_notifications = self.driver.find_element(By.CSS_SELECTOR, "div > button._a9--._a9_1")
        turn_off_notifications.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        sleep(4)
        see_followers = self.driver.find_element(By.CSS_SELECTOR, "a.x1a2a7pz._alvs._a6hd")
        see_followers.click()
        sleep(2)
        scroll_followers = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        scroll = 0
        while scroll < SCROLL_DOWN:  # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       scroll_followers)
            sleep(2)
            scroll += 1

    def follow(self):
        try:
            list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, "button._acas:not(._acao), a._acas:not("
                                                                           "._acao), a._acas:not(._acao):visited")
            for item in list_of_followers:
                print(item.text)
                if item.text == "Follow":
                    item.click()
                    sleep(5)
        except Exception as e:
            print(e)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
