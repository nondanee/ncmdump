# Netease Cloud Music Copyright Protection File Dump (Python version)

## 简介

<br /> Python版本解密ncm文件，其实说是什么DM加密是扯淡而已。要是真的玩上在线加密，那就没法离线播放了（正常人都知道的道理）
<br /> 不要泛滥哦嘤嘤嘤
<br /> 来自C++的版本，C++的版本和Python版本的原理相同，只是用了OpenSSL库，速度比Python更快。
<br /> 有兴趣可以试试做个PHP版本，毕竟是世界上最好的语言，可能比Python快多了（逃

## 依赖 pycrypto库 
<br />（你用C++版本可以用OpenSSL库或者Crypto++库，也可以手写AES128 ECB算法，然后再用JSON解析专辑名之类的）

```
pip(3) install pycrypto
```

## 嘤嘤嘤



#### - zhangbohan.dell@gmail.com
### 补充 
&emsp;&emsp;添加了一个pyqt的图形化界面，目前仅仅是可以使用，仍在不断优化  