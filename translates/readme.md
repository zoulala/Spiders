# 1.爬取goole翻译

## 说明

谷歌翻译直接通过request请求是获取不到结果的，需要tk值，tk值需要由问句+tkk值来生成。

- 获取tkk：

requests获取主页面，只需re正则在主页面上获取tkk值（之前需要通过js脚本来实现，[参考](https://blog.csdn.net/boyheroes/article/details/78681357)）

- 获取tk

通过js脚本实现
```javascript
var b = function (a, b) {
	for (var d = 0; d < b.length - 2; d += 3) {
		var c = b.charAt(d + 2),
			c = "a" <= c ? c.charCodeAt(0) - 87 : Number(c),
			c = "+" == b.charAt(d + 1) ? a >>> c : a << c;
		a = "+" == b.charAt(d) ? a + c & 4294967295 : a ^ c
	}
	return a
}

var tk =  function (a,TKK) {
	//console.log(a,TKK);
	for (var e = TKK.split("."), h = Number(e[0]) || 0, g = [], d = 0, f = 0; f < a.length; f++) {
		var c = a.charCodeAt(f);
		128 > c ? g[d++] = c : (2048 > c ? g[d++] = c >> 6 | 192 : (55296 == (c & 64512) && f + 1 < a.length && 56320 == (a.charCodeAt(f + 1) & 64512) ? (c = 65536 + ((c & 1023) << 10) + (a.charCodeAt(++f) & 1023), g[d++] = c >> 18 | 240, g[d++] = c >> 12 & 63 | 128) : g[d++] = c >> 12 | 224, g[d++] = c >> 6 & 63 | 128), g[d++] = c & 63 | 128)
	}
	a = h;
	for (d = 0; d < g.length; d++) a += g[d], a = b(a, "+-a^+6");
	a = b(a, "+-3^+b+-f");
	a ^= Number(e[1]) || 0;
	0 > a && (a = (a & 2147483647) + 2147483648);
	a %= 1E6;
	return a.toString() + "." + (a ^ h)
}
```

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
