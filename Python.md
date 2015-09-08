#Pythonについての備忘録

`ps aux | grep ○`
  * ○のアプリケーションが動いているか、動いていなければ出ない。

### 開発環境を整える
  1. python2.7は最初から入っている
  2. flaskはpipまたはeasy_installをインストールしてからだ
  3. ネットで`get-pip.py`をダウンロードし、
  4. 端末で`sudo python get-pip.py`を実行し、
  3. `sudo apt-get install python-pip`でインストール、そのあと
  4. `sudo pip install flask`といった感じ
