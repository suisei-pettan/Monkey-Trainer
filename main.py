import requests
import time
import pygame

# 目标URL
url = "https://lk.realmemobile.com/api/v2/"

# 音频文件路径
audio_file = "moonlight.mp3"

# 初始化 pygame 的混音模块
pygame.mixer.init()

while True:
    try:
        # 发送 GET 请求，设置超时时间为5秒
        response = requests.get(url, timeout=5)

        # 如果不是 504 状态码，则播放音频
        if response.status_code != 504:
            print(f"请求成功，状态码：{response.status_code}")

            # 加载并播放音频
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            # 等待音频播放完成
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        else:
            print("状态码 504，继续重试...")

    except requests.exceptions.Timeout:
        continue

