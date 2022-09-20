#!/usr/bin/python3

###Color Sample###

#pixels.fill((255, 0, 0))   :red
#pixels.fill((255, 0, 255)) :pink
#pixels.fill((0, 255, 255)) :waterblue
#pixels.fill((0, 255, 255)) :yellow
#pixels.fill((0, 255, 0))   :green
#pixels.fill((0, 0, 255))   :blue




###関数###

#pixels = neopixel.NeoPixel(Pin, 光らす範つまり光らすマス指定, brightness=LED全体の明るさをintで, auto_write=False pr True, pixel_order=neopixel.GRB)
#pixels[0] = ((R,G,B))                          :最初の人マスを光らす　特定の

#pixels.fill((R,G,B))                           :光らす範囲まで光らす

#pixels.show()                                  :auto_writeがFalseの場合、この関数で光らすことが可能



##AdafruitNeoPixelの公式サイトから引用しそれを翻訳したり工夫したりして紹介してます


###Smaple code###

#!/usr/bin/python3

import board
import neopixel
import time
import random

num_pixels = 47

pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.4, auto_write=False, pixel_order=neopixel.GRB) #board.D18 = GPIO18 ピンの12番>
colors = [0, 255, 128] #RGBの値を適当に書き込み

def wheel(pos):
    # 0～255の値を入力
    # r - g - b - rといろを買える仕組みにする
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if neopixel.GRB in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def clear_pix():
    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
    pixels.show()

try:
    while True: #無限におりゃーーー
        pixels.fill((random.choice(colors), random.choice(colors), random.choice(colors))) #ランダムにリストから抽出
        pixels.show()
        time.sleep(1)
        pixels.fill((random.choice(colors), random.choice(colors), random.choice(colors)))
        pixels.show()
        time.sleep(1)
        pixels.fill((random.choice(colors), random.choice(colors), random.choice(colors)))
        pixels.show()
        time.sleep(1)
        rainbow_cycle(0.001) #レインボーーーーーーーーーーーーーーーーーーーーーー
except KeyboardInterrupt:
    clear_pix()
    print("Finish!!")