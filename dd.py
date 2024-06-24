
from wxauto import WeChat
import time

# 实例化微信对象
wx = WeChat()

# 指定监听目标
listen_list = ['席好好',
               '席月婷',
               'ZHW',
               '潘骏',
               '周晨旭']


# 持续监听消息，并且收到消息后回复“收到”
wait = 2 # 设置10秒查看一次是否有新消息
for i in listen_list:
    wx.AddListenChat(who=i)  # 添加监听对象


while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        one_msgs = msgs.get(chat)   # 获取消息内容
        # ===================================================
        # 处理消息逻辑
        # 
        # 处理消息内容的逻辑每个人都不同，按自己想法写就好了，这里不写了
        # 
        # ===================================================
        
        # 回复收到
        for msg in one_msgs:
            if msg.type == 'friend':
                chat.SendMsg('【自动回复】好的')  # 回复收到
    time.sleep(wait)
