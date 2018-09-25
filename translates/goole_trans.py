import requests
import urllib
import re
import json
import execjs

class Goole_translate():
    def __init__(self):
        self.url_base = 'https://translate.google.cn'
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
        self.get_tkk()

    def get_tkk(self):
        page = requests.get(self.url_base, headers= self.headers )
        tkks = re.findall(r"TKK='(.+?)';", page.text)
        if tkks:
            self.tkk = tkks[0]
            return self.tkk
        else:
            raise ('no found tkk')

    def translate(self, query_string):
        last_url = self.get_last_url(query_string)
        response = requests.get(last_url, headers=self.headers)
        if response.status_code != 200:
            self.get_tkk()
            last_url = self.get_last_url(query_string)
            response = requests.get(last_url, headers=self.headers)

        content = response.content # bytes类型
        text = content.decode()  # str类型  , 两步可以用text=response.text替换
        dict_text = json.loads(text)  # 数据是json各式
        result = dict_text[0][0][0]
        return result

    def get_tk(self, query_string):
        tem = execjs.compile(open(r"gettk.js").read())
        tk = tem.call('tk', query_string, self.tkk)
        return tk

    def query_string(self, query_string):
        '''将字符串转换为utf8格式的字符串，本身已utf8格式定义的字符串可以不需要'''
        query_url_trans = urllib.parse.quote(query_string)  # 汉字url编码, 转为utf-8各式
        return query_url_trans

    def get_last_url(self, query_string):
        url_parm = 'sl=en&tl=zh-CN'
        for uchar in query_string:
            if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
                url_parm = 'sl=zh-CN&tl=en'
                break

        url_param_part = self.url_base + "/translate_a/single?"
        url_param = url_param_part + "client=t&"+ url_parm+"&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=3&tsel=3&kc=0&"
        url_get = url_param + "tk=" + str(self.get_tk(query_string)) + "&q=" + str(self.query_string(query_string))
        return url_get

if __name__=="__main__":
    query_string = 'how are you'
    gt = Goole_translate()
    en = gt.translate(query_string)
    print(en)



