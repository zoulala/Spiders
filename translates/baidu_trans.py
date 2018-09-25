# coding=utf-8
import requests
import json

class Baidu_translate():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"

    def get_lang(self,query_string):
        '''自动检测语言'''
        data = {'query':query_string}
        response = requests.post(self.lang_detect_url, data=data, headers=self.headers)
        return json.loads(response.text)['lan']

    def translate(self,query_string):
        '''翻译'''
        lang = self.get_lang(query_string)
        data = {"query":query_string,"from":"zh","to":"en"} if lang== "zh" else {"query":query_string,"from":"en","to":"zh"}
        response = requests.post(self.trans_url, data=data, headers=self.headers)
        result = json.loads(response.text)["trans"][0]["dst"]
        return result


if __name__ == '__main__':
    query_string = 'how are you'
    bt = Baidu_translate()
    en = bt.translate(query_string)
    print(en)
