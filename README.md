
# AC

AtCoder にトライするための環境と、トライした結果のコードの墓場

# Docker Image

## about this docker image

Python3.4.3 Environment  for AtCoder  
FROM python:3.4.3  
https://hub.docker.com/_/python?tab=tags&page=1&name=3.4.3


# About AtCoder python3 rule

https://atcoder.jp/contests/abc001/rules
```
言語
-Python3 (3.4.3)- → Python3 (3.8.2)

ライブラリ
Python2 / Python3	scikits	apt-get install python-scikits-learn で入るもの
Python3	numpy	apt-get install python3-numpy で入るもの
Python3	scipy	apt-get install python3-scipy で入るもの
```

-202002現在、Python3.4に標準で入ってくるpipは、 `scipy==0.13.3` に対応しておらず、また、`scikits-learn` の latest もインストール不可のため、このdockerファイルではインストールしない  
`numpy==1.8.2` のみ利用可能-  


### pull official image

```
$ docker pull python:3.4.3
```

### build & container start

```
$ docker-compose up ac_python
```


### container start

```
$ docker-compose start
```

### login to container

```
$ ./exec.sh
```

### push image to Docker.hub

```
$ docker push mollinaca/personal:ac_python
```
