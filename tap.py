# -*- coding: utf-8 -*-
import wda
import time
import random
import os

#device_url 根据WebDriverAgentWda启动返回给出的IP和Port
device_url ='http://localhost:8100/' 
c = wda.Client(device_url)  
s = c.session() 

# 仅针对667x375pt,具体屏幕，具体计算
def choose(jump_index,sleep_time):
    time.sleep(sleep_time) #ui渲染比较慢，需要延时点击
    choose_postion = [360,430,500,570]
    s.tap(160, choose_postion[jump_index])

def next_quiz():
    time.sleep(random.uniform(6.5, 7));
    os.remove('question.hortor.net/question/bat/fightResult')
    s.tap(200, 480)
    time.sleep(1)
    s.tap(200, 650)