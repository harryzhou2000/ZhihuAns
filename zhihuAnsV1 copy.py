# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:41:46 2020

@author: zxw
"""
# 引入必要的库
from operator import mod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import re
import pandas as pd
import datetime

from sqlalchemy import false, true


def get_driver():
    try:
        return webdriver.PhantomJS()
    except Exception:
        option = webdriver.ChromeOptions()
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        return webdriver.Chrome(options=option)


# 得到登录的cookie
def login_cookie():
    driver = get_driver()
    driver.set_page_load_timeout(20)
    driver.set_script_timeout(20)
    LOGIN_URL = 'https://www.zhihu.com/'
    driver.get(LOGIN_URL)
    time.sleep(2)
    input("请登录后按 Enter")
    cookies = driver.get_cookies()
    jsonCookies = json.dumps(cookies)
    # 下面的文件位置需要自己改
    with open('./out.txt', 'w') as f:
        f.write(jsonCookies)
    driver.quit()

# 再次登录


def login():
    driver.set_page_load_timeout(20)
    driver.set_script_timeout(20)
    LOGIN_URL = 'https://www.zhihu.com/'
    driver.get(LOGIN_URL)
    time.sleep(2)
    # 下面的文件位置需要自己改，与上面的改动一致
    f = open('./out.txt')
    cookies = f.read()
    jsonCookies = json.loads(cookies)
    for co in jsonCookies:
        driver.add_cookie(co)
    driver.refresh()
    time.sleep(2)

# 爬取某问题下的所有答案


def get_answers(question_url):
    global df

    # number_text = driver.find_element_by_partial_link_text('查看全部').text
    # number_text = driver.find_element_by_xpath(
    #     '/html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/h4/span').text
    # /html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/h4/span
    # number = int(re.search('[0-9]+,[0-9]+', number_text).group())
    number = 10000000
    # driver.find_element_by_partial_link_text('查看全部').click()

    for k in range(min(number, 50000)):
        xpathList = "/html/body/div[1]/div/main/div/div/div[3]/div[2]/div/div"

        # xpath = '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[{}]/div/div[2]/div[1]/span'.format(
        #     k+1)
        xpath = '/html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div/div[{}]/div/div/div[2]/div[1]/span'.format(
                k+1)
        xpathLoc = '/html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div/div[{}]/div/div/div[2]/div[2]/div'.format(
            k+1)
        xpathUp = '/html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div/div[{}]/div/div/div[2]/div[3]/span'.format(
            k+1)
# /html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div
#/html/body/div[1]/div/main/div/div
        # /html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/span
        # /html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span

        # /html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/span

        # /html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div
        # /html/body/div[1]/div/main/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div
        # got = True
        # while 1:
        #     try:
        #         if(got):
        #             elementT = WebDriverWait(driver, 1000).until(
        #                 EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "知乎隐私保护指引")))
        #             element = WebDriverWait(driver, 2).until(
        #                 EC.presence_of_element_located((By.XPATH, xpath)))
        #             elementLoc = WebDriverWait(driver, 10).until(
        #                 EC.presence_of_element_located((By.XPATH, xpathLoc)))
        #             elementUp = WebDriverWait(driver, 10).until(
        #                 EC.presence_of_element_located((By.XPATH, xpathUp)))
        #         else:
        #             element = WebDriverWait(driver, 100).until(
        #                 EC.presence_of_element_located((By.XPATH, xpath)))
        #             elementLoc = WebDriverWait(driver, 10).until(
        #                 EC.presence_of_element_located((By.XPATH, xpathLoc)))
        #             elementUp = WebDriverWait(driver, 10).until(
        #                 EC.presence_of_element_located((By.XPATH, xpathUp)))
        #         break
        #     except Exception:
        #         time.sleep(0.2)
        #         # js = "window.scrollTo(0,document.body.scrollHeight)"
        #         # driver.execute_script(js)
        #         js = "window.scrollTo(1,document.body.scrollHeight)"
        #         driver.execute_script(js)
        #         js = "window.scrollTo(0,document.body.scrollHeight)"
        #         driver.execute_script(js)
        #         js = "window.scrollTo(1,document.body.scrollHeight)"
        #         driver.execute_script(js)
        #         time.sleep(0.2)
        #         got = False
        #         pass

        # answer = element.text
        # loc = elementLoc.text
        # # 下面的文件位置需要自己改，保存到你想要的位置
        # file = open(
        #     './outAns{}.txt'.format(k+1), 'w', encoding='utf-8')
        # upSearch = re.search('[0-9]+', elementUp.text)
        # if upSearch is not None:
        #     nUp = int(upSearch.group())
        # else:
        #     nUp = 0
        # file.write(answer + "\n" + loc + '\n' + str(nUp))
        # file.close()
        # print('answer ' + str(k+1) + ' collected!')
        # df = df.append(
        #     {'ans': [answer], 'ups': nUp}, ignore_index=True)
        if k % 1 == 0:
            time.sleep(0.2)
            # js = "window.scrollTo(0,document.body.scrollHeight)"
            # driver.execute_script(js)
            js = "window.scrollTo(1,document.body.scrollHeight)"
            driver.execute_script(js)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            driver.execute_script(js)
            js = "window.scrollTo(1,document.body.scrollHeight)"
            driver.execute_script(js)
            time.sleep(0.2)
            pass


if __name__ == "__main__":
    df = pd.DataFrame(columns=('ans', 'ups'))
    # 设置你想要搜索的问题
    question_url = 'https://www.zhihu.com/question/530784320'
    # login_cookie()
    driver = get_driver()
    # login()
    # driver.get(question_url)
    get_answers(question_url)
    df.to_csv(
        f'result_{datetime.datetime.now().strftime("%Y-%m-%d")}.csv', index=False)
