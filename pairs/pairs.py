# -*- coding: utf-8 -*-
import datetime
import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # オプションを使うために必要
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import user

        
def func():
    I=0
    #自動ログイン開始
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    #chro =  webdriver.Chrome(executable_path=r'D:\masa\Anaconda3\chromedriver')#,chrome_options=opt)
    chro =  webdriver.Chrome(chrome_options=opt)
    chro.get("https://pairs.lv/#/login")
    #Facebookページ遷移〜ペアーズログインページ遷移
    chro.find_element_by_xpath('//*[@id="root"]/div[1]/main/div/div[1]/button/span').click()
    time.sleep(1)
    handle_array = chro.window_handles
    chro.switch_to.window(handle_array[-1])
    email=chro.find_element_by_name('email')
    email.send_keys(user.mail)
    password=chro.find_element_by_name('pass')
    password.send_keys(user.password)
    time.sleep(3)
    chro.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input').click()
    time.sleep(10)
    chro.switch_to.window(handle_array[-2])
    #src= "https://pairs.lv/#/search/one/%s"%str(I)
    chro.get('https://pairs.lv/search')  
    time.sleep(5)
    chro.get('https://pairs.lv/search')
    time.sleep(5)
    chro.get('https://pairs.lv/search')
    time.sleep(5)
    
    
    # In[12]:
    
    
    row=0
    for i in range(0,11):
        try:
            chro.find_element_by_xpath('/html/body/div[1]/div[1]/main/ul/li['+str(i)+']/div/div/a[1]/div/div[2]/div').click()       
            break
        except:
            continue
    
    time.sleep(1+random.random())
    #１０００人に到達するまで繰り返す（足跡間隔はランダムで5〜10秒の間）
    cnt=int(400*random.random())+700
    I=cnt
    handle_array = chro.window_handles
    chro.switch_to.window(handle_array[-1])
    
    
    # In[ ]:
    zahyo={}
    row=0
    for i in range(1,11):
        try:
            yazirushi=chro.find_element_by_xpath('//*[@id="dialog-root"]/div['+str(i)+']/div/div[1]/div/div[3]/div[2]/a')
            href=yazirushi.click()  
            row=i
            break
        except:
            continue
    layout=1
    cnt=0
    while I >1:
        I=I-1
        try:
            time.sleep(2+0.6*random.random())
            href1=chro.find_element_by_xpath('//*[@id="dialog-root"]/div['+str(row)+']/div/div[1]/div/div[3]/div[2]/a').get_attribute('href')
            
            if href1 == None:
                raise Exception('error')
            href=href1
            #zahyo_click(zahyo,chro)
            chro.find_element_by_xpath('//*[@id="dialog-root"]/div['+str(row)+']/div/div[1]/div/div[3]/div[2]/a').click()  
        except:
            print(href)
            if chro.current_url!='https://pairs.lv/search':
                chro.back()
            time.sleep(5+0.6*random.random())
            chro.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5+0.6*random.random())
            print(href)
            li=href.split('/')
            ui=chro.find_element_by_xpath('//*[@id="root"]/div[1]/main/ul')
            point_list=ui.find_elements_by_xpath("//a[@class='css-opde7s']")
            s=len(point_list)-10
            for _ in range(10):
                try:
                    check=point_list[s].get_attribute('class')
                    print(check)
                    if check!=None:
                        point_list[s].click()  
                    break
                except:
                    s=s-1
                    continue
            """
            for _ in range(5):
                try:
                    check=chro.find_element_by_xpath('/html/body/div[1]/div[1]/main/ul/li['+layout+']/div/div/a[1]').get_attribute('class')
                    print(check)
                    if check!=None:
                        chro.find_element_by_xpath('/html/body/div[1]/div[1]/main/ul/li['+layout+']/div/div/a[1]').click()  
                    
                    break
                except:
                    layout+=1
                    print(layout)
                    continue
            layout = layout-4
                
            #chro.find_element_by_xpath('//a[ends-with(@href,"'+li[len(li)-1]+'")]').click()  
            for i in range(0,15):
                try:

                    href=chro.find_element_by_xpath('//*[@id="dialog-root"]/div['+str(i)+']/div/div[1]/div/div[3]/div[2]/a').click()  
                    row=i
                    break
                except:
                    continue
            continue
        """
        time.sleep(3+0.6*random.random())
        print(str(I)+href)
        
    
    
    # In[ ]:
    
    
    dt_now = datetime.datetime.now()
    print(dt_now)
    chro.close()
if __name__=='__main__':
    func()
    func() 
