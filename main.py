# -*- coding: utf-8 -*-
from watchdog.observers import Observer
from watchdog.events import *
import time
import json
import requests
import sql
import random 
import math
import tap


def get_question(findQuiz):
    time.sleep(1)
    response = json.load(findQuiz)
    findQuiz.close()
    os.remove('question.hortor.net/question/bat/findQuiz')
    question = response['data']['quiz']
    options = response['data']['options']
    print(question)

    hit_result = sql.sql_match_result('"%s"' % question)
    
    if hit_result:
        print('正确答案是: %s ' % hit_result)
        correct_index = options.index(hit_result)
        sleep_time = 4
        tap.choose(correct_index,sleep_time)
    else:
        search_question(question, options)
    
    return response


def search_question(question,options):
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    counts = []
    for i in range(len(options)):
        counts.append(req.text.count(options[i]))
    
    max_index = counts.index(max(counts))
    min_index = counts.index(min(counts))
    if counts ==[0,0,0,0]:
        print('sry,没有找到合适答案')
        random_index = math.floor(random.uniform(0, 4))
        sleep_time =2.5
        tap.choose(random_index,sleep_time)
    else:
        sleep_time = 3
        if '不' in question:
           # 请注意此题可能为否定题,否定题选第一个选项
            print("答案可能是：{0} 或者 {1}".format(options[min_index],options[max_index]))
            tap.choose(min_index,sleep_time)
        else:
            print("答案可能是：{0}".format(options[max_index]))
            tap.choose(max_index,sleep_time)
            


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        global quiz
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            file_name = event.src_path.split('/')[-1]
            if  file_name == 'findQuiz':
                with open('question.hortor.net/question/bat/findQuiz', encoding='utf-8') as findQuiz:
                    quiz = get_question(findQuiz)
            elif file_name == 'choose':
                with open('question.hortor.net/question/bat/choose', encoding='utf-8') as choose:
                    sql.sql_write(quiz)
            elif file_name == 'fightResult':
                tap.next_quiz()          

if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler,"./question.hortor.net",True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()