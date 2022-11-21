from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from webdriver_manager.chrome import ChromeDriverManager
import time, random, requests, traceback
from time import sleep
from lxml.html import fromstring
from itertools import cycle
from bs4 import BeautifulSoup


noOfAcc = int(input("No. of Accounts you want to Create: "))

print("Requesting Proxies:")


def get_proxy_list():
    noProxyies = int(
        input("How many Working Proxys do you want to add to the List  ? : ")
    )
    proxyList = []
    count = 0
    response = requests.get("https://free-proxy-list.net")
    bs = BeautifulSoup(response.text, "lxml")
    table = bs.find("table")
    rows = table.find_all("tr")

    for row in rows:
        ip = row.contents[0].text
        port = row.contents[1].text
        state = row.contents[3].text
        anonym = row.contents[4].text
        conn = row.contents[6].text

        if conn == "yes" and (anonym == "anonymous" or anonym == "elite proxy"):
            line = "http:" + ip + ":" + port
            proxies = {"http": line, "https": line}
        try:
            testIP = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=3)
            resIP = testIP.json()["origin"]
            origin = resIP.split(",")
            if origin[0] == ip:
                print("Proxy Works! Adding Proxy to proxylist.txt")
                proxyList.append(ip + ":" + port)
                count += 1
                if count == noProxyies:
                    break

        except:
            print("Proxy isn't working! skipping ...")
    with open("proxylist.txt", "w") as f:
        for proxy in proxyList:
            f.write("%s\n" % proxy)


answer = input("Do you want ot create a new proxy list Y/N : ")
if answer == "Y" or answer == "y":
    get_proxy_list()
elif answer == "N" or answer == "n":
    print("Using current proxylist.txt(*Make sure is not Empty ! It won't work!)")
else:
    quit()


def rand_proxy():
    proxy = random.choice(open("proxylist.txt").read().split())
    return proxy


proxies = rand_proxy()


i = 0

while noOfAcc > i:

    firstName = random.choice(open("FirstnNamesList.txt").read().split())
    lastName = random.choice(open("LastNamesList.txt").read().split())
    fullName = firstName + " " + lastName
    username = (
        firstName
        + lastName
        + "."
        + str(random.randint(1, 100))
        + str(random.randint(1, 1000))
    )
    password = open("Password.txt").readline()
    email = random.choice(open("Emails.txt").read().split())
    print("\n \n Connecting to Proxy: " + str(proxies) + "\n")

    chrome_options = webdriver.ChromeOptions()
    proxy = rand_proxy()
    chrome_options.add_argument(f"--proxy-server={proxy}")
    url = "https://www.instagram.com/accounts/emailsignup/"
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    browser = webdriver.Chrome(PATH, options=chrome_options)
    browser.get(url)
    print(rand_proxy())

    print("\n \n Instagram Webpage Opened \n \n")
    sleep(3)

    emailIn = browser.find_element(
        By.NAME,
        value="emailOrPhone",
    )
    sleep(1)
    emailIn.send_keys(email)
    sleep(4)

    print("\n \n Your randomize Email:" + email + "\n \n")

    fullNameIn = browser.find_element(
        By.NAME,
        value="fullName",
    )
    fullNameIn.send_keys(fullName)

    sleep(5)
    print("\n \n Your randomize Full Name is: " + fullName + "\n \n")
    usernameIn = browser.find_element(
        By.NAME,
        value="username",
    )
    usernameIn.send_keys(username)
    print("\n \n Your randomize Username is: " + username + "\n \n")
    sleep(4)

    passwordIn = browser.find_element(
        By.NAME,
        value="password",
    )
    passwordIn.send_keys(password)
    print("\n \n Pa1ssword Entred is : " + password + "\n \n")
    sleep(2)
    try:
        signUp = browser.find_element(
            By.XPATH,
            value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/button",
        )
    except:
        signUp = browser.find_element(
            By.XPATH,
            value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button",
        )

    signUp.click()
    sleep(5)

    setYear = random.randint(20, 46)
    setMonth = random.randint(1, 12)
    setDay = random.randint(1, 27)

    yearEl = Select(browser.find_element(By.XPATH, value='//*[@title="Year:"]'))
    monthEl = Select(browser.find_element(By.XPATH, value='//*[@title="Month:"]'))
    dayEl = Select(browser.find_element(By.XPATH, value='//*[@title="Day:"]'))

    yearEl.select_by_index(setYear)
    print("\n Years Entred : " + str(setYear) + "\n")
    sleep(1)
    monthEl.select_by_index(setMonth)
    print("\n Month Entred  : " + str(setMonth) + "\n")
    sleep(1)
    dayEl.select_by_index(setDay)
    print("\n Date Entred : " + str(setDay) + " \n")
    sleep(5)
    nextButton = browser.find_element(
        By.XPATH,
        value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button",
    )
    nextButton.click()
    sleep(100)

    with open("username.txt", "w") as f_output:
        f_output.write(username)
    browser.close()

    i = i + 1
