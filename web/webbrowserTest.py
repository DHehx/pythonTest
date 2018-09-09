import webbrowser
import requests
webbrowser.open("https://www.google.com/search?hl=zh-CN&tbm=isch&source=hp&biw=1536&bih=758&ei=cYSTW5OcD-ua0wKam6mgDQ&q=monkey+D+luffy&oq=monkey+D+luffy&gs_l=img.3..0j0i30k1l9.23961.35581.0.35986.18.14.0.4.4.0.241.2110.2-9.9.0....0...1ac.1.64.img..5.13.2127.0..0i12k1.0.BiJ0I-V0UfM") #调用默认浏览器打开指定URL
res = requests.get('https://www.google.com/')
res.raise_for_status()
playFile = open('Google.html9','wb')
for chunk in res.iter_content(1000000):
    playFile.write(chunk)
playFile.close()