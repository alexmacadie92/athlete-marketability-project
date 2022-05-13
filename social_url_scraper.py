#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 20:42:19 2021

@author: alexmacadie
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
from time import sleep


# =============================================================================
# INPUTS
# =============================================================================


# PROVIDE PATH WHERE CHROMEDRIVER IS SAVED

DRIVER_PATH = ''  ### PASTE YOUR CHROMEDRIVER PATH HERE
        

# PROVIDE LIST OF NAMES TO LOOP THROUGH

names = [
'LeBron James',
'Lionel Messi'
]


# =============================================================================
# MAIN CODE - LOOPS THROUGH EACH NAME AND COLLECTS LINKS
# =============================================================================

options = Options()
options.headless = False
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

twitter = []
instagram = []
facebook = []
youtube = []
tiktok = []
linkedin = []
check = []



for i in range(0,len(names)):
    driver.get('https://www.google.com/search?q='+names[i])
    soup = BeautifulSoup(driver.page_source, "html.parser")
    twit = 0
    inst = 0
    face = 0
    you = 0
    tik = 0
    linked = 0
    
    ### CHECKS IF LINK IS LISTED IN GOOGLE PROFILE SECTION
    
    for j in range(0,len(soup.findAll("g-link", class_="fl"))):
        sleep(randint(1,2))
        link = soup.findAll("g-link", class_="fl")[j].findAll("a")[0].attrs["href"]
 
            
        if "instagram" in link:
            instagram.append(link)
            check.append(0)
            inst += 1
            
        elif "twitter" in link:
            twitter.append(link)
            twit += 1
            
        elif "facebook" in link:
            facebook.append(link)
            face += 1
            
        elif "youtube" in link:
            youtube.append(link)
            you += 1

        elif "tiktok" in link:
            tiktok.append(link)
            tik += 1
            
        elif "linkedin" in link:
            linkedin.append(link)
            linked += 1
    
    ### IF NOT SEARCHES FOR LINK TO THAT PLATFORM INDIVIDUALLY        
    
    if twit == 0:
        sleep(randint(1,2))
        driver.get('https://www.google.com/search?q='+names[i]+ ' Twitter')
        soup = BeautifulSoup(driver.page_source, "html.parser")
        try:
            twitter.append("https://www.twitter.com/"+soup.findAll("h3")[0].get_text().split('@',1)[1].split(')')[0])
        except:
            twitter.append("NULL")
        
    if inst == 0:
        sleep(randint(1,2))
        driver.get('https://www.google.com/search?q='+names[i]+ ' Instagram')
        soup = BeautifulSoup(driver.page_source, "html.parser")
        try:
            instagram.append("https://www.instagram.com/"+soup.findAll("h3")[0].get_text().split('@',1)[1].split(')')[0])
            check.append(1)
        except:
            instagram.append("NULL")
            check.append(1)
        
    if face == 0:
        sleep(randint(1,2))
        driver.get('https://www.google.com/search?q='+names[i]+ ' Facebook page -profiles -m.facebook')
        soup = BeautifulSoup(driver.page_source, "html.parser")
        try:
            facebook.append(soup.findAll("div", class_="tF2Cxc")[0].findAll("a")[0].attrs["href"])
        except:
            facebook.append("NULL")
        
    if linked == 0:
        sleep(randint(1,2))
        driver.get('https://www.google.com/search?q='+names[i]+ ' LinkedIn')
        soup = BeautifulSoup(driver.page_source, "html.parser")
        try:
            linkedin.append(soup.findAll("div", class_="tF2Cxc")[0].findAll("a")[0].attrs["href"])
        except:
            linkedin.append("NULL")
        
    if you == 0:
        sleep(randint(1,2))
        driver.get('https://www.youtube.com/results?search_query=' +names[i]+ '&sp=EgIQAg%253D%253D' )
        soup = BeautifulSoup(driver.page_source, "html.parser")
        try:
            if len(soup.find("div", {"id": "info-section"}).findAll("div", class_="badge badge-style-type-verified style-scope ytd-badge-supported-renderer")) == 1:
                youtube.append("https://www.youtube.com"+ soup.findAll("a", class_="channel-link yt-simple-endpoint style-scope ytd-channel-renderer")[0].attrs["href"])
            else:
                youtube.append("NULL")
        except:
            youtube.append("NULL")
        
    sleep(randint(1,2))

    if tik == 0:
        sleep(randint(1,2))    
       
        driver.get('https://www.google.com/search?q='+names[i]+ ' TikTok account')
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        try:
            if "tiktok" in soup.findAll("div", class_="yuRUbf")[0].findAll("a")[0].attrs["href"]:
            
                try:
        
                    tiktok.append("https://www.tiktok.com/@"+soup.findAll("h3")[0].get_text().split('@',1)[1].split(')')[0])
                except:
                    tiktok.append("NULL")
                    
            else:
                tiktok.append("NULL")
        except:
            tiktok.append("NULL")
            
            
        
driver.quit() 
        
df = pd.DataFrame({'Athlete':names,'Facebook ID':facebook, 'Twitter ID':twitter, 'Instagram ID':instagram, 'YouTube ID':youtube, 'TikTok ID':tiktok, 'LinkedIn ID':linkedin})
print(df)


