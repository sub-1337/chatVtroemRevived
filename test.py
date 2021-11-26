from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
import os
import time 


proxy = "socks4://77.122.57.126:1080"

#prox = Proxy()
#prox.proxy_type = ProxyType.MANUAL
#prox.proxy_autoconfig_url = proxy
#prox.http_proxy = proxy
#prox.socks_proxy = proxy
#prox.set_preference('network.proxy.socks_version', 4)
#prox.ssl_proxy = "ip_addr:port"

def install_firefox_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.socks", PROXY_HOST)
    fp.set_preference("network.proxy.socks_port", int(PROXY_PORT))
    fp.update_preferences()
    return webdriver.Firefox(firefox_profile=fp, executable_path="F:\\Documents\\Projects\\chatVtroemRevived\\geckodriver.exe")

#capabilities = webdriver.DesiredCapabilities.FIREFOX
#prox.add_to_capabilities(capabilities)

#This example requires Selenium WebDriver 3.13 or newer
def tryToWrite(ip_port):
    with install_firefox_proxy(ip_port.split(":")[0], ip_port.split(":")[1]) as driver:
        wait = WebDriverWait(driver, 10)
        driver.delete_all_cookies()
        try:
            driver.get("https://chatvdvoem.ru/")
        except:
            return "Bad"
        try:
            WebDriverWait(driver,15).until(EC.invisibility_of_element_located((By.ID, "topics-loading-spinner")))
        except:
            return "Fail"
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'topic')))
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'chat_start')))
        topic = driver.find_element_by_id("topic")
        topic.send_keys("лол")
        button = driver.find_element_by_id("chat_start")
        button.click()
        #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'status-chat-started')))
        #topic = driver.find_element_by_id("status-chat-started")
        # WebDriverWait(driver).until(EC.presence_of_element_located((By.ID, "log"))) #status-chat-started Чат начат, text, but-send, @ended-message
        #WebDriverWait(driver).until(EC.visibility_of((By.ID, "status-chat-started")))    
        # topics-loading-spinner    
        WebDriverWait(driver,600).until(EC.invisibility_of_element_located((By.ID, "status-chat-started")))
        #WebDriverWait(driver).until(EC.visibility_of((By.ID, "status-chat-started")))
        #driver.implicitly_wait(10)
        # nickname    
        #WebDriverWait(driver,600).until(EC.visibility_of_element_located((By.ID, "captcha")))
        try:
            WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.ID, "topic-current-chat")))
        except:
            return "Fail"
        textF = driver.find_element_by_id("text")
        textF.send_keys("лол")
        button = driver.find_element_by_id("but-send")
        button.click()
        WebDriverWait(driver,60).until(EC.invisibility_of_element_located((By.Class, "ended-message")))
        #WebDriverWait(driver, 1000).until(EC.text_to_be_present_in_element_value((By.ID, 'topic'), "\"Аноним\""))
        return "Win"

proxylist = [
    "184.185.2.190:4145",
    "72.217.216.239:4145",
    "139.59.1.14:1080",
    "5.252.161.48:1080",
    "159.203.61.169:1080",
    "184.181.217.204:4145",
    "186.126.73.238:1080",
    "128.199.202.122:1080",
    "8.135.28.152:1080",
    "72.221.172.203:4145",
    "72.221.232.155:4145",
    "179.49.57.150:6667",
    "154.16.202.22:1080"
]

fails = 0
proxyN = 0
while(True):
    if (fails >= 4):
        if proxyN >= len(proxylist):
            proxyN += 1
            fails = 0
        else:
            break
    res = tryToWrite(proxylist[proxyN])
    if (res == "Win"):
        break
    if (res == "bad"):
        continue
    if (res == "Fail"):
        fails += 1

