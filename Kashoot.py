import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import threading
import platform

print("                                      ")
print("  _  __         _                 _   ")
print(" | |/ /        | |               | |  ")
print(" | ' / __ _ ___| |__   ___   ___ | |_ ")
print(" |  < / _` / __| '_ \ / _ \ / _ \| __|")
print(" | . \ (_| \__ \ | | | (_) | (_) | |_ ")
print(" |_|\_\__,_|___/_| |_|\___/ \___/ \__|")
print("                                      ")
print("Kahoot Smasher, written by Lunarixus")
print("Credit to frogsandcode for the WebDriver func")
print("Credit to Selenium for the WebDriver")

generate_names = input("Would you like to generate insulting names? ")

class createBot:
    def __init__(self, pin, name):
        chrome_options = Options()
        prefs = {"profile.exit_type" : "Normal"}
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)
        print("\nConnecting to game at " + pin + " as " + name)
        self.driver.get('http://www.kahoot.it')
        self.pin = pin
        self.driver.find_element_by_id('game-input').send_keys(pin)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.driver.implicitly_wait(2)
        self.nameIn = self.driver.find_element_by_id("nickname")
        self.nameIn.send_keys(name)
        self.nameIn.send_keys(Keys.RETURN)

        while True:
            pass

pin = str(input("Input Kahoot pin: "))
botNum = int(input("How many bots? "))

if generate_names.lower() == "":
    baseName = str(input("What should they be named? "))
else:
    baseName = ""

for x in range(botNum):
    if generate_names.lower() != "":
        request = urllib.request.urlopen("https://insult.mattbas.org/api/adjective")
        insult = "you're " + request.read().decode('ascii')
        botThread = threading.Thread(target=createBot, args=(pin, insult))
    else:
        botThread = threading.Thread(target=createBot, args=(pin, str(baseName + str(x))))
    botThread.start()
