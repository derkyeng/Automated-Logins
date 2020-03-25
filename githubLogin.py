from selenium import webdriver
import loginInfo

browser = webdriver.Chrome()
browser.get('https://github.com/login')

def loginTwitter():
    userButton = browser.find_element_by_xpath('//*[@id="login_field"]')
    userButton.send_keys(loginInfo.githubUser)

    passButton = browser.find_element_by_xpath('//*[@id="password"]')
    passButton.send_keys(loginInfo.githubPass)

    loginButton = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
    loginButton.click()

if __name__ == '__main__':
    loginTwitter()
