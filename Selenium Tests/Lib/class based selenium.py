import collections
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import webdriver_manager.chrome

from selenium.webdriver.support import expected_conditions as EC
import time

import time

driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())


class Links:
    def __init__(self, ar):
        self.url = ar
        self.p = ["2160", "1440", "1080"]

    def get(self):
        time.sleep(0.1)
        vals = []
        vids = []
        element = driver.find_element(By.CLASS_NAME, "uvmspn7")
        element.click()
        text = driver.title
        text = str(text + "\n")
        time.sleep(0.1)
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            if ".mp4" in link.get_attribute("href"):
                vids.append(link.get_attribute("href"))
        for i in reversed(vids):
            x = i
            vals = [x, text]
            break
        print(vals)
        return vals


def buildclass(ar):
    x = 1
    videodl = []
    vids = []
    vals = []
    l = []
    comb = {}
    for i in ar:
        v = Browser(i, ".mp4")
        v.navigate()

        l = {x: Links(v)}
        vids = l[x].get()
        comb[vids[1]] = {vids[0]}

        x = x + 1
##################
######test vers#########
##################
        if (x >= 5):
            break

    return comb


##################
'''
def looper(ar):
    x = 0
    links = []
    for i in ar:
        x += 1
        if x <= 15:
            v = Browser(i, ".mp4")
            v.navigate()
            element = driver.find_element(By.CLASS_NAME, "uvmspn7")
            vel = str(driver.find_element(By.ID, "video-info"))
            element.click()
            p = ["2160", "1440", "1080"]
            time.sleep(0.2)
            lnks = driver.find_elements(By.NAME, "a")
            x = 0
            for lnk in reversed(lnks):
                arrays = []
                x = x + 1
                if "mp4" in lnk.get_attribute("href"):
                    arrays.append(lnk.get_attribute("href"))
                for i in arrays:
                    for pix in p:
                        if pix in i:
                            links[info].append(i)
                            x = x + 1
                            break
            continue
        break
    print(links)
    return links
'''


def writer(v):
    with open('links.md', 'w') as f:
        f.write("\n")
        f.close()
    with open('links.md', "a") as f:
        for key, vals in v.items():
            f.write(key, vals)
        f.close()


def login():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "login"))
        )
    finally:
        time.sleep(0.5)
        element = driver.find_element(By.NAME, "login")
        element.send_keys("samfisherirl")
        element = driver.find_element(By.NAME, "haslo")
        element.send_keys("321eagle")
        element = driver.find_element(By.NAME, "Submit")
        element.click()


class Browser:
    def __init__(self, url, keyword):
        self.url = url
        self.keyword = keyword

    def navigate(b):
        driver.get(b.url)
        return driver

    def getlinks(a):
        lnks = driver.find_elements(By.TAG_NAME, "a")
        arrays = []
        for lnk in lnks:
            # get_attribute() to get all href
            if a.keyword in lnk.get_attribute("href"):
                arrays.append(lnk.get_attribute("href"))  # remove duplicate
        array = [item for item, count in collections.Counter(arrays).items() if count > 1]
        return array


# identify elements with tagname <a>
# traverse list
pw = Browser("https://www.eporner.com/login/", "")
pw.navigate()
login()
vr = Browser("https://www.eporner.com/cat/vr-porn/milf/SORT-top-rated/3/", "video-")
vr.navigate()
array = vr.getlinks()
val = buildclass(array)
writer(val)
driver.quit()
