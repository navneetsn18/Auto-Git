import sys,os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
folderName = str(sys.argv[1])

browser = webdriver.Chrome("./chromedriver")
browser.get('http://github.com/login')


def remove():
    browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(username)
    browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(password)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    browser.get('https://github.com/'+ username + "/" + folderName + '/settings')
    browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0].click()
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(username+"/"+folderName)
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    browser.get("https://github.com/" + username)


if __name__ == "__main__":
    remove()