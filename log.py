from bs4 import BeautifulSoup
import requests
import time
import re
import sys
import datetime


def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr)
  return content[startIndex:endIndex]

def patientlist (gong_hao):
    '''主页'''
    log1hea = {
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
        'Host': '***',
        'Connection': 'Keep-Alive'
    }
    log1ur = '***'
    log1html = requests.get(url=log1ur, headers=log1hea)
    cooki = log1html.cookies
    cook = str(cooki)[27:97]

    log2hea = {
        'Host': '***',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
        'DNT': '1',
        'Referer': '***',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie':cook
    }
    log2ur = '***'
    log2html = requests.get(url=log2ur, headers=log2hea)

    TRELOADID = GetMiddleStr(log1html.text, 'logon.csp?TRELOADID=', '&TRELOAD=1')
    TPAGID = GetMiddleStr(log1html.text, 'CHANGEPASSWORD&TPAGID=', '&ID=\',false,')
    yearmonday = datetime.datetime.now().strftime('%Y-%m-%d')
    hourmin = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hourn = hourmin[-7]
    minn = hourmin[-5:-3]
    ClientTime = hourn + '%3A' + minn

    USERNAME = gong_hao[0]
    PASSWORD = gong_hao[1]

    longdata = 'TFORM=SSUserLogon&TPAGID=' + TPAGID + '&TEVENT=d1473iLogon&TOVERRIDE=&TDIRTY=1&TWKFL=&TWKFLI=&TWKFLL=&TWKFLJ=&TREPORT=&TRELOADID=' + TRELOADID + '&TFRAME=&RELOGON=&LocationListFlag=0&SSUSERGROUPDESC=&changeinlogonhosp=&Hospital=&ClientDate=' + yearmonday + '&ClientTime=' + ClientTime + '&USERNAME=' + USERNAME + '&PASSWORD=' + PASSWORD
    longdata1 = '\n' + longdata
    longdatalog = 'SSUserLogon&TPAGID=' + TPAGID + '&TEVENT=d1473iLogon&TOVERRIDE=&TDIRTY=1&TWKFL=&TWKFLI=&TWKFLL=&TWKFLJ=&TREPORT=&TRELOADID=' + TRELOADID + '&TFRAME=&RELOGON=&LocationListFlag=0&SSUSERGROUPDESC=&changeinlogonhosp=&Hospital=&ClientDate=' + yearmonday + '&ClientTime=' + ClientTime + '&USERNAME=' + USERNAME + '&PASSWORD=' + PASSWORD

    longdatalogcsp = 'TFORM=SSUserLogon&TPAGID=' + TPAGID + '&TEVENT=d1473iLogon&TOVERRIDE=&TDIRTY=1&TWKFL=&TWKFLI=&TWKFLL=&TWKFLJ=&TREPORT=&TRELOADID=' + TRELOADID + '&TFRAME=&RELOGON=&LocationListFlag=1&SSUSERGROUPDESC=&changeinlogonhosp=&Hospital=&ClientDate=' + yearmonday + '&ClientTime=' + ClientTime + '&USERNAME=' + USERNAME + '&PASSWORD=' + PASSWORD + "&DEPARTMENT=wcddwk-%CE%A2%B4%B4%B5%A8%B5%C0%CD%E2%BF%C6"


    log3hea = {
        'Host': '***',
        'Connection': 'keep-alive',
        'Content-Length': '285',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Origin': '***',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Referer': '***',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': cook
    }
    log3ur = '***'
    log3html = requests.post(url=log3ur, headers=log3hea, data=longdata1)
    cooki2 = log3html.cookies
    cook2 = str(cooki2)[27:97]

    log4hea = {
    'Host': '***',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
    'DNT': '1',
    'Referer': '***',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': cook2
    }
    log4ur = '***'
    log4html = requests.get(url=log4ur, headers=log4hea)

    log5hea = {
        'Host': '***',
        'Connection': 'keep-alive',
        'Content-Length': '340',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Origin': '***',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Referer': '***',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': cook2
    }
    log5ur = '***'
    longdata2 = longdata1 + "&DEPARTMENT=" + gong_hao[2]
    log5html = requests.post(url=log5ur, headers=log5hea, data=longdata2)

    #6页是标题页
    log6hea = {
        'Host': '***',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
        'DNT': '1',
        'Referer': '***',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': cook2
    }
    log6ur = '***'
    log6html = requests.get(url=log6ur, headers=log6hea)
    #列表项目
    TPAGID_search_fied_search = " ".join(re.findall('ClearDetails(.*?)查询', log6html.text, re.S))
    TPAGID_search_list_search = re.findall('\(\'(.*?)\',\'\'\)"', TPAGID_search_fied_search, re.S)[0]

    log7ur = '***'
    log7html = requests.get(url=log7ur, headers=log6hea)
    cooki3 = log6html.cookies
    cook3 = str(cooki3)[27:97]

    #log8html是患者未排序列表
    log8hea = {
        'Host': '***,
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
        'DNT': '1',
        'Referer': '***',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': cook3
    }
    log8ur = '***'
    log8html = requests.get(url=log8ur, headers=log8hea)    #.content.decode('GB2312')


    #   ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！下一步排序、访问地址、换账号登录、print (log8html.text)
    #  TPAGID_fied_search = " ".join(re.findall('TPAGID"(.*?)>', log8html, re.S))  # TPAGID登录页面的tgapid打开检索页面，检索页tgapid、TRELOADID用来post
    #   TPAGID_list_search = re.findall('"(.*?)"', TPAGID_fied_search, re.S)[0]

    cooki4 = log8html.cookies
    cook4 = str(cooki4)[27:97]

    log9hea = {
        'Host': '***',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
        'DNT': '1',
        'Referer': '***',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': cook4
    }
    log9ur = '***'
    log9html = requests.get(url=log9ur, headers=log9hea)

    log10hea = {
        'Host': '***',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
        'DNT': '1',
        'Referer': '***',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': cook4
    }
    log10ur = '***'
    log10html = requests.get(url=log10ur, headers=log10hea)
    #print(log10html.text)

    patientlishtml = log10html.text
    PatientID_fied = " ".join(re.findall('PatientID(.*?)>', patientlishtml, re.S))
    PatientID_list = re.findall('value="(.*?)"', PatientID_fied, re.S)

    EpisodeID_fied = " ".join(re.findall('EpisodeID(.*?)>', patientlishtml, re.S))
    EpisodeID_list = re.findall('value="(.*?)"', EpisodeID_fied, re.S)
    # for EpisodeID in EpisodeID_text:
    # print (EpisodeID)
    mradm_fied = re.findall('mradm(.*?)>', patientlishtml, re.S)
    mradm_list = re.findall('value="(.*?)"', " ".join(mradm_fied), re.S)

    PAAdmBedz_fied = " ".join(re.findall('"PAAdmBedz(.*?)/label>', patientlishtml, re.S))  # 床位号
    PAAdmBedz_list = re.findall('">(.*?)<', PAAdmBedz_fied, re.S)

    PAPMINamez_fied = " ".join(re.findall('"PAPMINamez(.*?)/A>', patientlishtml, re.S))  # 姓名
    PAPMINamez_list = re.findall('">(.*?)<', PAPMINamez_fied, re.S)

    PAPMISexz_fied = " ".join(re.findall('"PAPMISexz(.*?)/label>', patientlishtml, re.S))  # 性别
    PAPMISexz_list = re.findall('">(.*?)<', PAPMISexz_fied, re.S)

    Agez_fied = " ".join(re.findall('"Agez(.*?)/label>', patientlishtml, re.S))  # 年龄
    Agez_list = re.findall('">(.*?)<', Agez_fied, re.S)

    Diagnosisz_fied = " ".join(re.findall('"Diagnosisz(.*?)/label>', patientlishtml, re.S))  # 诊断
    Diagnosisz_list = re.findall('">(.*?)<', Diagnosisz_fied, re.S)

    PAAdmDatez_fied = " ".join(re.findall('"PAAdmDatez(.*?)/label>', patientlishtml, re.S))  # 年龄
    PAAdmDatez_list = re.findall('">(.*?)<', PAAdmDatez_fied, re.S)
    PAAdmDatez_list_new = []
    for PAAdmDat in PAAdmDatez_list:
        today = datetime.datetime.today()
        PAAdmDateday = datetime.datetime.strptime(PAAdmDat, '%Y-%m-%d')
        ndays_ruyuan = today - PAAdmDateday
        PAAdmDat = '第' + str(ndays_ruyuan.days+1) + '天'
        PAAdmDatez_list_new.append(PAAdmDat)


    PAAdmReasonz_fied = " ".join(re.findall('"PAAdmReasonz(.*?)/label>', patientlishtml, re.S))  # 病人类型
    PAAdmReasonz_list = re.findall('">(.*?)<', PAAdmReasonz_fied, re.S)

    Amountz_fied = " ".join(re.findall('"Amountz(.*?)/label>', patientlishtml, re.S))  # 费用
    Amountz_list = re.findall('">(.*?)<', Amountz_fied, re.S)

    Chargez_fied = " ".join(re.findall('"Chargez(.*?)/label>', patientlishtml, re.S))  # 余额，是否欠费
    Chargez_list = re.findall('">(.*?)<', Chargez_fied, re.S)

    zipinfo = zip(PatientID_list,EpisodeID_list,mradm_list,PAAdmBedz_list,PAPMINamez_list,PAPMISexz_list,Agez_list,Diagnosisz_list,PAAdmDatez_list_new,PAAdmReasonz_list,Amountz_list,Chargez_list)
    # for patientinfo in zipinfo:  # PatientID_list,EpisodeID_list,mradm_list,患者床号，姓名，性别，年龄，诊断，入院n日，（手术后几日），病人类型，费用,余额是否欠费

    return(zipinfo)
