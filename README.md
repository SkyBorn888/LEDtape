# LED_Tape



Systemdとrc.localの二つを使った起動時に光らす方法も書いてるよ
詳しくはライセンスを見てね。


PythonでAdafuiltNeoPixelを使ったサンプルコードです。

ちなみに配線の接続部分がGrand 5V GPIO この三つのLEDテープでお願いします。USBなど他のものにやろうとするとどうなるかわかりません。
LEDテープ名忘れてしまいました。パッケージが見つかり次第書きます


てことで
 # Install module whitch is adaruit foundation modules to LED tapeだ！

$sudo pip3 install adafruit-circuitpython-neopixel

python3.7
Raspberry Pi 3b+   4でもいけるよ



# おまけ
ラズパイ起動時に光らしたくない？？
まじでおすすめ！linuxが大好きsystemdでの設定方法を書きまーーーす！！

crontabとかrc.localで起動時やればいいじゃんってねww
まぁどれでもいいんやけど、例えばBluetoothを使って起動時光らしたいとかっだたらSystemdの方が良いんだって話ぃぃぃいぃ

はい！

超簡単
まず初めにファイルに実行権限をあたえてください
$chmod 755 LED_Tape/LEDtape_Samples.py

次に

$cd /usr/lib/systemd/system/

このディレクトリ下にunitファイルを作成します
今回は

$sudo touch LED_tape.service
$sudo chmod 751 LED_tape.service

LED_tape.serviceをつくりそこに下記のように書き込みます

[Unit]
Description = LEDtape
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/LED_tape/LEDtape_Samples.py
Restart=always
Type=idle

[Install]
WantedBy=multi-user.target

これが書けたら

$sudo systemctl enable LED_tape.service

これでおｋ　あとは再起動してみてください
