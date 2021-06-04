#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import time
import pygame.mixer

print("何分待ちますか ")
n=input()
if n.isdecimal():
   n=int(n)
print("何秒待ちますか ")
m=input()
if m.isdecimal():
   m=int(m)


def time_start():
    print("n分m秒スタート ")
    time_sta = time.time()
    time.sleep(60*n+m)
# 時間計測終了
    time_end = time.time()
# 経過時間（秒）
    tim = time_end- time_sta
    Sound()
    print(tim)


def Sound():
    pygame.mixer.init() #初期化
    pygame.mixer.music.load('Kalimba.mp3') #読み込み
    pygame.mixer.music.play(-1) #ループ再生（引数を1にすると1回のみ再生）
    input()
    pygame.mixer.music.stop() #終了   



root = tk.Tk()                # 窓を作る
root.title("Timer")   # 窓のタイトルを設定
root.geometry("640x480")
#ウィンドウだけ出来た。タイトルはTimer

label = tk.Label(root, text="スタート")  # ラベルを作成

#ラベルを表示
label.pack()   

button = tk.Button()                        # ボタンを作成
button["text"] = "スタート"         # ボタンにラベルを設定
button["command"] = lambda: time_start() # ボタンの動作を設定
button.pack()   

root.mainloop()  # ループ（対話型環境では不要）


# In[ ]:




