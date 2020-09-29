# getemall_yt
# this program is made for downloading all videos in a channel.
# you can change video format and quality
# this program require  ffmpeg , youtube-dl and chrome driver. download  these and put in windows file or add as  enviroment path
# https://chromedriver.chromium.org
# https://youtube-dl.org
# https://ffmpeg.org
# creator: sabrey
import sys
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


driver = webdriver.Chrome()

#list of videos' link
link_list = []

def get_links(url):
    driver.get(url + "/videos")
    ht = driver.execute_script("return document.documentElement.scrollHeight;")
    while True:
        prev_ht = driver.execute_script("return document.documentElement.scrollHeight;")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        ht = driver.execute_script("return document.documentElement.scrollHeight;")
        if prev_ht == ht:
            break

    links = driver.find_elements_by_xpath('//*[@id="video-title"]')

    for link in links:
        link_list.append(link.get_attribute("href"))

#you can change youtube-dl command https://youtube-dl.org
def download_videos():
    for element in link_list:
        print(element)
        command = "youtube-dl " + element
        os.system(command)


def main():
    print("Youtube Video Scrapper  by Sabrey \n")

    url = sys.argv[1]

    get_links(url)

    download_videos()





if __name__ == "__main__":
    main()
