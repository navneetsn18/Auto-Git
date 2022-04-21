# Create.py
import sys,os,time
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
folderName = str(sys.argv[1])

browser = webdriver.Chrome("./chromedriver")
browser.get("http://github.com/login")
def create():
    browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]").send_keys(username)
    browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]").send_keys(password)
    browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]").click()
    browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/summary").click()
    browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/details-menu/a[1]").click()
    browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input").send_keys(folderName)
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()
    browser.close()

if __name__=="__main__":
    create()
