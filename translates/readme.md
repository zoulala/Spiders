# 1.爬取goole翻译

## 说明

谷歌翻译直接通过request请求是获取不到结果的，需要tk值，tk值需要由问句+tkk值来生成。

- 获取tkk：

requests获取主页面，只需re正则在主页面上获取tkk值（之前需要通过js脚本来实现，[参考](https://blog.csdn.net/boyheroes/article/details/78681357)）

- 获取tk

通过js脚本实现：gettk.js


- 最终地址

将tk值和需要翻译的句子代人如下格式

中-英 :
>https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=xxxxxx&q=xxxxxxx

英-中：
>https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=xxxxxx&q=xxxxxxx

程序中简单增加了中英文判断。

- requests获取结果

获取的结果在三维的列表中，list[0][0][0]即为所需的结果

##注意

频繁访问可能被封，没有测试过，可以设置延时或ip代理

## 参考
http://www.cnblogs.com/by-dream/p/6554340.html

https://blog.csdn.net/boyheroes/article/details/78681357

# 2.爬取百度翻译

- 自动检测中英文

- 获取百度翻译结果


## 参考
https://blog.csdn.net/blues_f/article/details/79319461


# 3.中文-英文-中文
通过中-英-中可以产生相似问答对语料。
- q_zh:中文问句
- g_en:谷歌对中文问句中-英翻译
- b_zh:百度对谷歌结果进行英-中翻译

```buildoutcfg
q_zh: 下周有什么好产品？
g_en: What are the good products next week?
b_zh: 下周的好产品是什么？


q_zh: 第一次使用，额度多少？
g_en: What is the amount of the first use?
b_zh: 第一次使用的数量是多少？


q_zh: 我什么时候可以通过微粒贷借钱
g_en: When can I borrow money from micro-credit?
b_zh: 我什么时候可以从小额信贷中借钱？


q_zh: 借款后多长时间给打电话
g_en: How long does it take to make a call after borrowing?
b_zh: 借钱后打电话需要多长时间？


q_zh: 没看到微粒贷
g_en: Didn't see the micro-credit
b_zh: 没有看到小额信贷


q_zh: 原来的手机号不用了，怎么换
g_en: The original mobile phone number is not used, how to change
b_zh: 原来的手机号码没有用，怎么改
```


