# -*- coding: utf-8 -*-
import sqlite3
import json
import time
import os

conn = sqlite3.connect('./questions',check_same_thread=False)

def sql_match_result(question):
  sql_cmd = 'select * from questions where question=' + question
  cursor = conn.execute(sql_cmd)
  right =''
  for a in cursor:
    right = a[1]

  if not right=='' :
    return right
  else:
    return False
	
def sql_write(quiz):
    with open('question.hortor.net/question/bat/choose', encoding='utf-8') as f:
      time.sleep(1)
      response = json.load(f)
      f.close()
      os.remove('question.hortor.net/question/bat/choose')
      question = quiz['data']['quiz']
      index = int(response['data']['answer']) -1
      answer = quiz['data']['options'][index]
      print('正确答案是: %s ,正在写入数据库...'% answer)
      try:
        conn.execute("insert into questions(question,answer)values('%s','%s')" % (question,answer))
        conn.commit()
        print('写入数据库成功\n')
      except:
        print('该问题已存在数据库中，跳过\n')