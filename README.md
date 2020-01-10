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
####   以上为原作者内容，fork 自 [lianglixin/ncmdump](https://github.com/lianglixin/ncmdump)
<hr />

### 补充 
#### - zhangbohan.dell@gmail.com

&emsp;&emsp;添加了一个pyqt的图形化界面，目前仅仅是可以使用，仍在不断优化  
#### 目前功能
1. 一个简陋的图形化窗口
2. 支持文件夹添加，会识别文件夹中的ncm文件，并将其转为一个同名的MP3和一个同名的jpg，保存到指定文件夹
3. 添加多线程支持，但是目前功能有限

#### 计划未来版本
1. 优化图形化界面，添加更多功能
2. 将jpg专辑图片保存mp3内部(网易云高版本可能不会存储图片信息)


#### 技术栈
1. python
2. AES128 ECB算法
3. PyQt5

#### ui转化
```bash
pyuic5 -o file.py file.ui
```
