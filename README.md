# Instagram-Account-Creator
Instagram-MultiAccountCreator


THIS BOT IS FOR FUN AND EDUCATIONAL PURPOSES PLEASE BE NICE WITH IT!

A bot that Creates Accounts for Instagram!
It Automatically Authenticates the Proxy with Webdriver Selenium by Autofilling the Pop-up Login tab of Proxy !!

![image](https://user-images.githubusercontent.com/118709832/203001714-a90954a2-ad14-4fdf-ad9b-834f162dc6aa.png)


Hi there ! This is a selenium bot that Creates Instagram Accounts . It saves the credentials in a .txt file !

-First option - You can Generate Accounts using free Proxy, the Bot will grab free proxys from "https://free-proxy-list.net" and it will
test them if they Work. If yes the Ip is going to be added on the proxylist.txt and then randomly used to Create a account.

-Second options - ProxyGenerateAccount.py
As we know free proxys usually DO NOT WORK but in order to rotate requests with different proxys to the Website you have to
have a list of paid proxys that work or you want to buy some proxys. Second option is the right One.



*HOW TO INSTALL*

git clone https://github.com/beephole/instagram-Account-Creator.git

cd  instagram-Account-Creator

pip install -r requirements.txt

python generateAccount.py - for free proxies

or

python proxyGenerateAccount.py - for paid proxies




https://user-images.githubusercontent.com/118709832/202999434-39890d61-acd6-4632-9188-4e6e002f9eb8.mp4







*WORK TO BE DONE BEFORE STARTING THE BOT*

1. Download Chromedriver(Check for Version of Chromedriver and your Chrome Browser it should be the same)

2. Check your Chromedriver PATH and edit with your PATH at the script

   line 103 - generateAccount.py
   
   line 80 - proxyGenerateAccount.py
   
   Ex. Download Chromedriver and move it from downloads to Program Files (x86) 
   and the PATH should be ok!
   
   

3. Generate virtual Emails at websites like https://tenmail.org and copy-paste them at Emails.txt
   (You want to get the Confirmation Code from IG, virtual Email is the easiest way!)
![image](https://user-images.githubusercontent.com/118709832/202995562-e15f668f-aec8-422d-bba2-8a4e0daf992b.png)



4. For Paid Proxies(With Authentication) - open proxyGenerateAccount.py script and enter details maually

   PROXY_HOST = "129.150.19.177" # rotating proxy or host
   
   PROXY_PORT = 15323 # port
   
   PROXY_USER = "proxyusername" # username
   
   PROXY_PASS = "proxypassword" # password
   
   
   
   ![image](https://user-images.githubusercontent.com/118709832/202996061-18e79d0f-6d4c-4235-a9b5-68ceebdf0b7d.png)


*PAY ATTENTION*

1. New Username is saved at username.txt
2. Free Proxys are added to proxylist.txt and then choosen randomly .
3. Password is going to be the same for all accounts.(You can change it.)
4. Too many requests with the same proxy ,may get banned the proxy from the website you sending requests at,
   You have to have over 5 proxys , the bot will choose a random proxy each time a account is being created !
5. REMEMBER YOU HAVE TO GO TO YOUR VIRTUAL EMAIL MAILBOX TO CHECK THE CONFIRMATION CODE AND ENTER IT MANUALLY!

"I’m always doing things I can’t do. That’s how I get to do them."

btc: 137L6AWxzsJ5eqsptGZx2yEfuznR9qntk3
