#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     downloadfile.py
# author:   zlw2008ok@126.com
# date:     2022/10/21
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import os
import time
import requests


url = "https://hita.omaha.org.cn/term/download?filename=疾病分类与代码国家临床版2.0&type=编码资源"
url = "https://hita.omaha.org.cn/term/download?filename=ICD-10 WHO(中文版)(2020)_结构化&type=编码资源"
url = "https://hita.omaha.org.cn/term/download?filename=国际疾病分类第十一次修订本(ICD-11)中文版(201812)&type=编码资源"
url = "https://hita.omaha.org.cn/term/download?filename=手术操作分类与代码细目表(2011)&type=编码资源"


headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # "Content-Length": "45",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "identitys=4; grading=4; Hm_lvt_c5f999fb6da6b6ecd0233092b251f516=1652840057; Hm_lpvt_c5f999fb6da6b6ecd0233092b251f516=1652840057; member_UU=0381f598-201f-4335-8597-72f4aedd00a8; member_UN=qihl@xnewtech.com; identitys=4; grading=4; JSESSIONID=7c13883e-b073-4dfa-8e6b-95df4f266250",
        "Host": "hita.omaha.org.cn",
        "Origin": "https://hita.omaha.org.cn",
        # "Referer": "https://hita.omaha.org.cn/resource/mdDetail?hitaId=H20001&metadataType=%E5%80%BC%E5%9F%9F&type=1&userDefined=1&num=201",
        "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
}

response=requests.get(url,headers=headers)

leng=len(list(response.iter_content(1024)))  #下载区块数
if(leng==1):								#如果是1 就是空文件 重新下载
      print('下载失败,重新下载')

filename = "xxx.xlsx"
with open(filename, 'wb') as f:
    for chunk in response.iter_content(1024):  # 防止文件过大，以1024为单位一段段写入
        f.write(chunk)


# 文件名 及结构 参考如下：
"""
<div class="public-main">
	<div class="public-box" style="padding-bottom:0;">
		<div class="industryNavTitle primaryTitle" style="font-weight: bold;color:#303030;">行业术语资源</div>
		<div class="standardClassBox">
			<ul>
				<li class="active" data-type="standardClass1">临床所见</li>
				<li data-type="standardClass2">操作</li>
				<li data-type="standardClass3">药品</li>
				<li data-type="standardClass5">中医</li>
				<li data-type="standardClass4">其他</li>
				<p class="clear"></p>
			</ul>
		</div>
		<div class="standardTerm" style="background: #F0F2F5;padding-bottom: 4px;">
			<!-- 分类筛选 -->
			<div class="industryResourcesClassify">
				<div class="standardTermClass standardClass1">
					<div class="industryResourcesTypeBtn IRTSelect" data-type="1" data-class="ICD-10">ICD-10</div>
					<div class="industryResourcesTypeBtn" data-type="3" data-class="ICD-11-MMS">ICD-11-MMS</div>
					<div class="clear"></div>
				</div>

				<div class="standardTermClass standardClass2" style="display: none;">
					<div class="industryResourcesTypeBtn" data-type="2" data-class="ICD-9-CM-3">ICD-9-CM-3</div>
					<div class="industryResourcesTypeBtn" data-type="5" data-class="医疗服务项目">医疗服务项目</div>
					<div class="industryResourcesTypeBtn" data-type="9" data-class="临床检验项目">临床检验项目</div>
					<div class="clear"></div>
				</div>
				<div class="standardTermClass standardClass3" style="display: none;">
					<div class="industryResourcesTypeBtn" data-type="4" data-class="ATC">ATC</div>
					<div class="industryResourcesTypeBtn" data-type="6" data-class="国家药品编码本位码">国家药品编码本位码</div>
					<div class="industryResourcesTypeBtn" data-type="7" data-class="国家基本药物目录">国家基本药物目录</div>
					<div class="industryResourcesTypeBtn" data-type="8" data-class="医保药品目录">医保药品目录</div>
					<div class="industryResourcesTypeBtn" data-type="12" data-class="医保药品分类与代码">医保药品分类与代码</div>
					<div class="clear"></div>
				</div>

				<div class="standardTermClass standardClass5" style="display: none;">
					<div class="industryResourcesTypeBtn" data-type="13" data-class="中药方剂编码">中药方剂编码</div>
					<div class="industryResourcesTypeBtn" data-type="14" data-class="中医病证分类与代码">中医病证分类与代码</div>
					<div class="industryResourcesTypeBtn" data-type="15" data-class="中医临床名词术语">中医临床名词术语</div>
					<div class="industryResourcesTypeBtn" data-type="16" data-class="中医临床诊疗术语">中医临床诊疗术语</div>
					<div class="clear"></div>
				</div>
				<div class="standardTermClass standardClass4" style="display: none;">
					<div class="industryResourcesTypeBtn" data-type="10" data-class="CHS-DRG">CHS-DRG</div>
					<div class="industryResourcesTypeBtn" data-type="11" data-class="常用临床医学名词">常用临床医学名词</div>
					<div class="clear"></div>
				</div>
			</div>

			<div class="industryResourcesBox">

				<!-- ICD-10 -->
				<div class="industryResourcesTypeBox industryResourcesMutual" id="industryResourcesICD10">
					<table class="standardSourceTable">
						
						<!-- <tr class="standardSourceTableTr" data-type="2" data-name="《疾病分类与代码(修订版)》亚目表 全国2011版" data-type="编码资源">
							<td style="width:calc(100% - 300px);">《疾病分类与代码(修订版)》亚目表 全国2011版</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
						</tr> -->

						<tr class="standardSourceTableTr" data-type="2" data-name="ICD-10 WHO(中文版)(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">ICD-10 WHO(中文版)(2020)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3"></span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="疾病诊断分类与代码医保版2.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">疾病诊断分类与代码医保版2.0</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="疾病分类与代码国家临床版2.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">疾病分类与代码国家临床版2.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="疾病分类与代码国家标准版1.1" data-type="编码资源">
							<td style="width:calc(100% - 300px);">疾病分类与代码国家标准版1.1</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="GB/T 14396-2016 疾病分类与代码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">GB/T 14396-2016 疾病分类与代码</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="疾病分类与代码国家临床版1.1" data-type="编码资源">
							<td style="width:calc(100% - 300px);">疾病分类与代码国家临床版1.1</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京市疾病诊断名称与代码标准V7.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京市疾病诊断名称与代码标准V7.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>
						<tr class="standardSourceTableTr" data-type="2" data-name="北京疾病分类与代码临床版V6.01" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京疾病分类与代码临床版V6.01</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="疾病分类与代码国家标准版1.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">疾病分类与代码国家标准版1.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="全国疾病分类与代码修订版(2011)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">全国疾病分类与代码修订版(2011)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="全国疾病分类与代码1.3" data-type="编码资源">
							<td style="width:calc(100% - 300px);">全国疾病分类与代码1.3</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="上海疾病分类与代码更新版(2013)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">上海疾病分类与代码更新版(2013)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="全国RC020-ICD-10诊断编码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">全国RC020-ICD-10诊断编码</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="全国RC021-ICD-10形态学编码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">全国RC021-ICD-10形态学编码</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京RC020-ICD-10诊断编码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京RC020-ICD-10诊断编码</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京RC021-ICD-10形态学编码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京RC021-ICD-10形态学编码</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京疾病分类与代码标准V5.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京疾病分类与代码标准V5.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广东疾病分类与代码(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广东疾病分类与代码(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="疾病分类与代码国家临床版1.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">疾病分类与代码国家临床版1.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="济南卫生信息数据共享与交换规范值域代码：疾病分类与代码(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">济南卫生信息数据共享与交换规范值域代码：疾病分类与代码(2019)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="上海疾病分类与代码标准库(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">上海疾病分类与代码标准库(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="云南疾病分类与代码国家临床版1.1扩展版(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">云南疾病分类与代码国家临床版1.1扩展版(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="云南损伤中毒外部原因国家临床版1.1扩展版(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">云南损伤中毒外部原因国家临床版1.1扩展版(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>
					</table>
				</div>
				
				<!-- ICD-10 -->


				<!-- ICD-9 -->
				<div class="industryResourcesTypeBox" id="industryResourcesICD9">
					<table class="standardSourceTable">

						<tr class="standardSourceTableTr" data-type="2" data-name="手术操作分类与代码细目表(2011)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">手术操作分类与代码细目表(2011)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="手术操作分类与代码医保版2.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">手术操作分类与代码医保版2.0</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="手术操作分类与代码国家临床版1.1" data-type="编码资源">
							<td style="width:calc(100% - 300px);">手术操作分类与代码国家临床版1.1</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="手术操作分类与代码国家临床版2.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">手术操作分类与代码国家临床版2.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="手术操作分类代码国家临床版3.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">手术操作分类代码国家临床版3.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="手术操作分类代码国家临床版3.0修订版(2022)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">手术操作分类代码国家临床版3.0修订版(2022)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="全国手术操作分类与代码(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">全国手术操作分类与代码(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京住院病案首页手术操作分类与代码V6.01" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京住院病案首页手术操作分类与代码V6.01</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广东手术操作分类与代码(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广东手术操作分类与代码(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广东手术操作分类与代码(2016)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广东手术操作分类与代码(2016)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="山东医疗机构手术操作分类与代码(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">山东医疗机构手术操作分类与代码(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="山东手术操作分类与代码V6.01" data-type="编码资源">
							<td style="width:calc(100% - 300px);">山东手术操作分类与代码V6.01</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京住院病案首页手术操作分类与代码V5.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京住院病案首页手术操作分类与代码V5.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京住院病案首页手术操作分类与代码V6.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京住院病案首页手术操作分类与代码V6.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京RC022-ICD-9手术操作分类与代码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京RC022-ICD-9手术操作分类与代码</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="四川手术操作分类与代码(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">四川手术操作分类与代码(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="全国手术操作分类与代码维护版(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">全国手术操作分类与代码维护版(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="手术操作分类与代码国家临床版1.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">手术操作分类与代码国家临床版1.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="TCHIA 001-2017手术、操作分类与代码团体标准版" data-type="编码资源">
							<td style="width:calc(100% - 300px);">TCHIA 001-2017手术、操作分类与代码团体标准版</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="上海手术操作分类与代码标准库(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">上海手术操作分类与代码标准库(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="云南手术操作分类与代码国家临床1.1扩展版(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">云南手术操作分类与代码国家临床1.1扩展版(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京手术操作字典V7.0" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京手术操作字典V7.0</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>
					</table>
				</div>
				<!-- ICD-9 -->


				<!-- ICD-11 -->
				<div class="industryResourcesTypeBox" id="industryResourcesICD11">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="国际疾病分类第十一次修订本(ICD-11)中文版(201812)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国际疾病分类第十一次修订本(ICD-11)中文版(201812)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>
					</table>
				</div>
				<!-- ICD-11 -->

				<!-- ATC -->
				<div class="industryResourcesTypeBox" id="industryResourcesATC">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="3" data-name="解剖学治疗学及化学分类系统(2021)_OMAHA本地化版本" data-type="编码资源">
							<td style="width:calc(100% - 300px);">解剖学治疗学及化学分类系统(2021)_OMAHA本地化版本</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>
					</table>
				</div>
				<!-- ATC -->

				<!-- 国家药品编码本位码 -->
				<div class="industryResourcesTypeBox" id="industryResourcesGJypbm">
					<table class="standardSourceTable">

						<tr class="standardSourceTableTr" data-type="2" data-name="国家药品编码本位码(20220630)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国家药品编码本位码(20220630)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="国家药品编码本位码(20210930)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国家药品编码本位码(20210930)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="国家药品编码本位码(20201231)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国家药品编码本位码(20201231)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<!-- <td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td> -->
						</tr>
					</table>
				</div>
				<!-- 国家药品编码本位码 -->

				<!-- 国家基本药物目录 -->
				<div class="industryResourcesTypeBox" id="industryResourcesGJypjbml">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="国家基本药物目录(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国家基本药物目录(2018)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
					</table>
				</div>
				<!-- 国家基本药物目录 -->

				<!-- 国家药品目录 -->
				<div class="industryResourcesTypeBox" id="industryResourcesListOfDrugs">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="国家基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国家基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="国家基本医疗保险、工伤保险和生育保险药品目录(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国家基本医疗保险、工伤保险和生育保险药品目录(2020)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="安徽省基本医疗保险、工伤保险和生育保险药品目录编码数据库(20210601)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">安徽省基本医疗保险、工伤保险和生育保险药品目录编码数据库(20210601)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="安徽省基本医疗保险、工伤保险和生育保险药品目录(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">安徽省基本医疗保险、工伤保险和生育保险药品目录(2018)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京市基本医疗保险工伤保险和生育保险药品目录(2017)">
							<td style="width:calc(100% - 300px);">北京市基本医疗保险工伤保险和生育保险药品目录(2017)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="甘肃省基本医保药品目录数据字典(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">甘肃省基本医保药品目录数据字典(2020)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="甘肃省城镇职工基本医疗保险工伤保险和生育保险药品目录(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">甘肃省城镇职工基本医疗保险工伤保险和生育保险药品目录(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广西基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广西基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>
						<tr class="standardSourceTableTr" data-type="2" data-name="广西基本医疗保险、工伤保险和生育保险药品目录(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广西基本医疗保险、工伤保险和生育保险药品目录(2020)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="贵州省基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">贵州省基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="贵州省基本医疗保险、工伤保险和生育保险药品目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">贵州省基本医疗保险、工伤保险和生育保险药品目录(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="海南省基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">海南省基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="海南省基本医疗保险、工伤保险和生育保险药品目录(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">海南省基本医疗保险、工伤保险和生育保险药品目录(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河南省基本医疗保险、工伤保险和生育保险药品目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河南省基本医疗保险、工伤保险和生育保险药品目录(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="黑龙江省基本医疗保险、工伤保险和生育保险药品目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">黑龙江省基本医疗保险、工伤保险和生育保险药品目录(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="湖北省基本医疗保险、工伤保险和生育保险药品目录(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">湖北省基本医疗保险、工伤保险和生育保险药品目录(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="吉林省基本医疗保险、工伤保险和生育保险药品目录(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">吉林省基本医疗保险、工伤保险和生育保险药品目录(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="江苏省基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">江苏省基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							<td class="textRight" width="150px"><!-- <span class="standardDown termDownListPublic3">结构化文件下载</span> --></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="江苏省基本医疗保险、工伤保险和生育保险药品目录数据库(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">江苏省基本医疗保险、工伤保险和生育保险药品目录数据库(2020)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="江苏省基本医疗保险、工伤保险和生育保险药品目录(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">江苏省基本医疗保险、工伤保险和生育保险药品目录(2018)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="江西省基本医疗保险、工伤保险和生育保险药品目录代码(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">江西省基本医疗保险、工伤保险和生育保险药品目录代码(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="辽宁省基本医疗保险、工伤保险和生育保险药品目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">辽宁省基本医疗保险、工伤保险和生育保险药品目录(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="宁夏回族自治区基本医疗保险、工伤保险和生育保险药品目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">宁夏回族自治区基本医疗保险、工伤保险和生育保险药品目录(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="青海省基本医疗保险、工伤保险和生育保险药品目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">青海省基本医疗保险、工伤保险和生育保险药品目录(2019)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="青海省基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">青海省基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="山东省基本医疗保险、工伤保险和生育保险药品目录(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">山东省基本医疗保险、工伤保险和生育保险药品目录(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="上海市基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">上海市基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="上海市基本医疗保险、工伤保险和生育保险药品目录(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">上海市基本医疗保险、工伤保险和生育保险药品目录(2017)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="四川省基本医疗保险、工伤保险和生育保险药品目录(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">四川省基本医疗保险、工伤保险和生育保险药品目录(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="新疆维吾尔自治区、新疆生产建设兵团基本医疗保险、工伤保险和生育保险药品目录(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">新疆维吾尔自治区、新疆生产建设兵团基本医疗保险、工伤保险和生育保险药品目录(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="云南省基本医疗保险、工伤保险和生育保险药品目录(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">云南省基本医疗保险、工伤保险和生育保险药品目录(2018)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广东省基本医疗保险、工伤保险和生育保险药品目录(2022)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广东省基本医疗保险、工伤保险和生育保险药品目录(2022)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广东省基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广东省基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						

						<tr class="standardSourceTableTr" data-type="2" data-name="广东省基本医疗保险、工伤保险和生育保险药品目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广东省基本医疗保险、工伤保险和生育保险药品目录(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河北省基本医疗保险、工伤保险和生育保险药品目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河北省基本医疗保险、工伤保险和生育保险药品目录(2021)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河北省基本医疗保险、工伤保险和生育保险药品目录(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河北省基本医疗保险、工伤保险和生育保险药品目录(2020)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河北省基本医疗保险、工伤保险和生育保险药品目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河北省基本医疗保险、工伤保险和生育保险药品目录(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>
					</table>
				</div>
				<!-- 国家药品目录 -->

				<!-- 其他医疗服务 -->
				<div class="industryResourcesTypeBox" id="industryResourcesMedicalService">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="安徽省医疗服务价格项目目录(2022)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">安徽省医疗服务价格项目目录(2022)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="安徽省基本医疗保险医疗服务项目目录(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">安徽省基本医疗保险医疗服务项目目录(2018)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京医疗服务价格项目(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京医疗服务价格项目(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="福建医疗服务价格(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">福建医疗服务价格(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="甘肃医疗服务项目价格(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">甘肃医疗服务项目价格(2017)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>


						<tr class="standardSourceTableTr" data-type="2" data-name="广东省基本医疗服务价格项目目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广东省基本医疗服务价格项目目录(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广东医疗机构基本医疗服务项目价格汇总表(2015)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广东医疗机构基本医疗服务项目价格汇总表(2015)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广西医疗服务项目价格(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广西医疗服务项目价格(2021)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="广西医疗服务项目(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">广西医疗服务项目(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="贵州省医疗服务价格目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">贵州省医疗服务价格目录(2021)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="贵州医疗服务价格表(2016)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">贵州医疗服务价格表(2016)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="海南省医疗服务价格(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">海南省医疗服务价格(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="海南医疗服务价格(2016)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">海南医疗服务价格(2016)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河北省城市公立医院医疗服务价格项目规范(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河北省城市公立医院医疗服务价格项目规范(2017)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河北医疗服务收费项目(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河北医疗服务收费项目(2020)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河北医疗服务价格项目(2015)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河北医疗服务价格项目(2015)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河南省医疗服务价格表(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河南省医疗服务价格表(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="河南省医疗服务收费标准(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">河南省医疗服务收费标准(2017)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="黑龙江医疗服务收费目录(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">黑龙江医疗服务收费目录(2020)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="黑龙江医疗服务价格(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">黑龙江医疗服务价格(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="湖北医疗服务价格(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">湖北医疗服务价格(2019)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="湖南省现行医疗服务价格项目目录(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">湖南省现行医疗服务价格项目目录(2020)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="湖南省现行医疗服务价格目录(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">湖南省现行医疗服务价格目录(2019)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="吉林医疗价格标准表(2011)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">吉林医疗价格标准表(2011)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="江苏基本医疗诊疗服务项目、医疗服务设施范围和支付标准(2010)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">江苏基本医疗诊疗服务项目、医疗服务设施范围和支付标准(2010)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="江西省医疗服务项目分类与代码(20210830)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">江西省医疗服务项目分类与代码(20210830)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="江西医疗服务价格手册(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">江西医疗服务价格手册(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="辽宁省省管公立医院医疗服务项目价格(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">辽宁省省管公立医院医疗服务项目价格(2017)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="内蒙古自治区医疗服务项目规范和价格(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">内蒙古自治区医疗服务项目规范和价格(2021)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="内蒙古自治区医疗服务项目价格表(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">内蒙古自治区医疗服务项目价格表(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="青海医疗服务价格目录(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">青海医疗服务价格目录(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="全国医疗服务价格项目规范(2012)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">全国医疗服务价格项目规范(2012)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<!-- <tr class="standardSourceTableTr" data-type="2" data-name="全国医疗服务项目分类与代码医保版(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">全国医疗服务项目分类与代码医保版(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
						</tr> -->

						<tr class="standardSourceTableTr" data-type="2" data-name="山东省省（部）属医疗机构医疗服务价格表(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">山东省省（部）属医疗机构医疗服务价格表(2020)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="山东医疗服务价格项目(2009)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">山东医疗服务价格项目(2009)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="山西省公立医疗机构医疗服务项目价格(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">山西省公立医疗机构医疗服务项目价格(2020)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="陕西省医疗服务项目价格(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">陕西省医疗服务项目价格(2021)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="陕西城市公立医院医疗服务项目价格(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">陕西城市公立医院医疗服务项目价格(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="上海医疗机构医疗服务项目和价格汇编(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">上海医疗机构医疗服务项目和价格汇编(2017)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="四川医疗收费目录(2016)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">四川医疗收费目录(2016)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="天津市医疗服务项目价格目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">天津市医疗服务项目价格目录(2021)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="天津医疗服务价格项目(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">天津医疗服务价格项目(2020)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="新疆维吾尔自治区医疗服务价格规范(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">新疆维吾尔自治区医疗服务价格规范(2017)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="云南省医疗服务项目分类代码(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">云南省医疗服务项目分类代码(2021)</td>
							
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="云南非营利性医疗服务价格(2016)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">云南非营利性医疗服务价格(2016)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="浙江省省级公立医院医疗服务价格项目汇总表(202205)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">浙江省省级公立医院医疗服务价格项目汇总表(202205)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="浙江省基本医疗保险医疗服务项目目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">浙江省基本医疗保险医疗服务项目目录(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="浙江省级公立医院医疗服务项目价格汇总表(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">浙江省级公立医院医疗服务项目价格汇总表(2019)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="中国医疗服务操作项目分类及编码CCHI(2010)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">中国医疗服务操作项目分类及编码CCHI(2010)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="重庆市基本医疗保险医疗服务项目目录(2021)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">重庆市基本医疗保险医疗服务项目目录(2021)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="重庆医疗服务价格项目(2015)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">重庆医疗服务价格项目(2015)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="宁夏回族自治区城市社区卫生服务机构医疗服务项目价格(试行)(2017)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">宁夏回族自治区城市社区卫生服务机构医疗服务项目价格(试行)(2017)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="兰州市医疗服务项目价格(2018)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">兰州市医疗服务项目价格(2018)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>

						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="北京手术等医疗服务项目价格收费表(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">北京手术等医疗服务项目价格收费表(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="济南市居民基本医疗保险普通门诊统筹诊疗项目目录(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">济南市居民基本医疗保险普通门诊统筹诊疗项目目录(2020)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="宁夏三甲医院医疗服务项目价格(2020)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">宁夏三甲医院医疗服务项目价格(2020)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
					</table>
				</div>
				<!-- 临床检验项目 -->

				<!-- 国家药品编码本位码 -->
				<div class="industryResourcesTypeBox" id="industryResourcesListClinicalCheckout">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="医疗机构临床检验项目目录(2013)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">医疗机构临床检验项目目录(2013)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="DB33T 903-2013 临床实验室试验项目分类与编码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">DB33T 903-2013 临床实验室试验项目分类与编码</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="临床检验项目分类与代码(wst102-1998)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">临床检验项目分类与代码(wst102-1998)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>
					</table>
				</div>
				<!-- 临床检验项目 -->
				
				<!-- CHS-DRG -->
				<div class="industryResourcesTypeBox" id="industryResourcesChsDrg">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="国家医疗保障局疾病诊断相关分组(CHS-DRG)分组方案(1.1版)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国家医疗保障局疾病诊断相关分组(CHS-DRG)分组方案(1.1版)</td>
							<td class="textRight" width="150px"><!-- <span class="standardDown termDownListPublic3">结构化文件下载</span> --></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="国家医疗保障疾病诊断相关分组(CHS-DRG)细分组(1.0版)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">国家医疗保障疾病诊断相关分组(CHS-DRG)细分组(1.0版)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
					</table>
				</div>

				<!-- 常用临床医学名词 -->
				<div class="industryResourcesTypeBox" id="industryResourcesMedicalNomenclature">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="常用临床医学名词(2019)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">常用临床医学名词(2019)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
							
						</tr>
					</table>
				</div>
				<!-- 医保药品分类与代码 -->
				<div class="industryResourcesTypeBox" id="ndustryResourcesClassifyOrCode">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="医保药品分类与代码(202208)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">医保药品分类与代码(202208)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
						<tr class="standardSourceTableTr" data-type="2" data-name="海南医保药品分类与代码(20210730)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">海南医保药品分类与代码(20210730)</td>
							<td class="textRight" width="150px"></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="江西省医保药品分类与代码(202011)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">江西省医保药品分类与代码(202011)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="医保药品分类与代码(202109)" data-type="编码资源">
							<td style="width:calc(100% - 300px);">医保药品分类与代码(202109)</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
					</table>
				</div>
				<!-- 医保药品分类与代码 -->

				<!-- 中药方剂编码 -->
				<div class="industryResourcesTypeBox" id="chineseMedicinePrescriptionCode">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="GBT 31773-2015 中药方剂编码规则及编码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">GBT 31773-2015 中药方剂编码规则及编码</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="GBT 31774-2015 中药编码规则及编码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">GBT 31774-2015 中药编码规则及编码</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
					</table>
				</div>
				<!-- 中药方剂编码 -->

				<!-- 中医病证分类与代码 -->
				<div class="industryResourcesTypeBox" id="classificationAndCodeOfTcmDiseaseSyndrome">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="《中医病证分类与代码》医保版对应《中医病证分类与代码》(GB_T 15657-2021)映射表" data-type="编码资源">
							<td style="width:calc(100% - 300px);">《中医病证分类与代码》医保版对应《中医病证分类与代码》(GB_T 15657-2021)映射表</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>

						<tr class="standardSourceTableTr" data-type="2" data-name="GB-T 15657-2021 中医病证分类与代码" data-type="编码资源">
							<td style="width:calc(100% - 300px);">GB-T 15657-2021 中医病证分类与代码</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
					</table>
				</div>
				<!-- 中医病证分类与代码 -->

				<!-- 中医临床名词术语 -->
				<div class="industryResourcesTypeBox" id="clinicalTermsOfTcm">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="20214265-T-468 中医临床名词术语" data-type="编码资源">
							<td style="width:calc(100% - 300px);">20214265-T-468 中医临床名词术语</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
					</table>
				</div>
				<!-- 中医临床名词术语 -->

				<!-- 中医临床诊疗术语 -->
				<div class="industryResourcesTypeBox" id="TraditionalChineseMdicineClinicalDiagnosisAndTreatmentTerm">
					<table class="standardSourceTable">
						<tr class="standardSourceTableTr" data-type="2" data-name="中医临床诊疗术语" data-type="编码资源">
							<td style="width:calc(100% - 300px);">中医临床诊疗术语</td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">结构化文件下载</span></td>
							<td class="textRight" width="150px"><span class="standardDown termDownListPublic3">源文件下载</span></td>
						</tr>
					</table>
				</div>
				<!-- 中医临床诊疗术语 -->
			</div>
		</div>
	</div>

		
"""
