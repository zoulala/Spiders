'''
通过翻译实现中文问句的相似问法，来产生相似问题对数据集。可用于语义相似模型训练。

goole翻译：中文-英文
baidu翻译：英文-中文

注意：本程序未设置ip代理，频繁访问谨防被封。（只做了简单的随机延迟措施）
'''
import time
import random
from goole_trans import Goole_translate
from baidu_trans import Baidu_translate

gt = Goole_translate()
bt = Baidu_translate()

r_file = 'data/zh.txt'
w_file = 'data/zh_en_zh.txt'
fw = open(w_file,'w',encoding='utf8')
with open(r_file,'r',encoding='utf8') as f:
    for line in f:
        r = random.random()*10
        time.sleep(r)
        ls = line.strip().split('\t')
        query_string = ls[0]
        g_en = gt.translate(query_string)
        b_zh = bt.translate(g_en)
        fw.write(query_string+'\t'+g_en+'\t'+b_zh+'\n')

        print('q_zh:',query_string)
        print('g_en:',g_en)
        print('b_zh:',b_zh)
        print('\n')
fw.close()

