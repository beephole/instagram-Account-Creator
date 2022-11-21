import os, zipfile, time, random, requests, traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from lxml.html import fromstring
from itertools import cycle


PROXY_HOST = "209.250.19.177"  # rotating proxy or host
PROXY_PORT = 12323  # port
PROXY_USER = "14a8f1241a1a5"  # username
PROXY_PASS = "ed023506d8"  # password


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (
    PROXY_HOST,
    PROXY_PORT,
    PROXY_USER,
    PROXY_PASS,
)


def get_chromedriver(use_proxy=False, user_agent=None):
    path = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        pluginfile = "proxy_auth_plugin.zip"

        with zipfile.ZipFile(pluginfile, "w") as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument("--user-agent=%s" % user_agent)
    driver = webdriver.Chrome(path, chrome_options=chrome_options)
    return driver


noOfAcc = int(input("No. of Accounts you want to Create: "))

print("Requesting Proxies:")

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

    print("\n \n Connecting to Proxy: \n")
    browser = get_chromedriver(use_proxy=True)
    url = "https://www.instagram.com/accounts/emailsignup/"
    browser.get(url)
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
    time.sleep(1000)
