# getemall_yt
# this program is made for downloading all videos in a channel.
# you can change video format and quality
# this program require  ffmpeg , youtube-dl and chrome driver. download  these and put in windows file or add as  enviroment path
# https://chromedriver.chromium.org
# https://youtube-dl.org
# https://ffmpeg.org
# creator: sabrey
import sys
from selenium import webdriver
import os
import subprocess
driver = webdriver.Chrome()


def main():
    print("Youtube Video Scrapper  by Sabrey \n")
    url = sys.argv[1]
   # command = "youtube-dl " + url
    
    print("downloading...")
   # os.system(command)
    subprocess.run(["youtube-dl", url], stdin=subprocess.DEVNULL)


if __name__ == "__main__":
    main()
