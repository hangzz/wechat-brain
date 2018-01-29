# wechat-brain


## 原理说明

### Charles抓包，
  * 获取 *https://question.hortor.net/question/bat/* 返回的json数据，
  * *Tools->Mirror* 保存为本地文件


### *watchdog*
  监测 *question.hortor.net/question/bat/* 下的文件
  *  *findQuiz* => 返回题目信息，查找答案
       
  *  *choose* => 返回正确答案，保存数据库

### 模拟点击
  * IOS
    * [WebDriverAgent](https://github.com/facebook/WebDriverAgent) 
    * [ATX 文档 - iOS 真机如何安装 WebDriverAgen](https://testerhome.com/topics/7220)
  * Android
    * [adb](http://adbshell.com/downloads)


## 数据库

* [数据库文件](./questions)
  
  





