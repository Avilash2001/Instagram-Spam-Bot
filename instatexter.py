from selenium import webdriver
from time import sleep
from secrets import username,password
from random import randint
class InstaSpamBot():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com")
        sleep(5)
        fb_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]')

        fb_btn.click()
        sleep(5)
        email_in=self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        password_in=self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        login_btn=self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()
        sleep(10)
        notif_prompt=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notif_prompt.click()
        sleep(3)
        direct_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
        direct_btn.click()
        sleep(5)
        adwait=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]')
        adwait.click()

    def action(self,i,times):    
        text_box=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        if i==0:
            text_box.send_keys(f'Hi! I am an intelligent software created by Avilash Ghosh. \nI will now send you {times} texts!\nThank You for your time!')
        else:
            text_box.send_keys(f'Text no: {i}')

        send_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        send_btn.click()
        

bot=InstaSpamBot()
bot.login()
times=int(input("Enter the number of times: "))
while True:
    for i in range(times+1):
        bot.action(i,times)
    choice=input("Wanna Go again?? (Y/N) ")
    if choice == 'N' or choice == 'n':
        break    