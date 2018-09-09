#! python3
#天天基金排行，近一年
import requests,os,bs4,pymysql


def saveDB(fundinfoList):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "mysql", "python", port=3306, use_unicode=1, charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 准备sql
    sqlStr = ''
    # try:
    for fundinfo in fundinfoList:
        if fundinfo != '':
            sqlStr = "INSERT INTO `python`.`eastmoneyFundRank` (`date`, `fundcode`, `rank`, `fundname`, `value`) VALUES ('%s', '%s', '%s', '%s', '%s');" %(
                fundinfo.get('date'), fundinfo.get('fundcode'), fundinfo.get("rank"), fundinfo.get("fundname"), fundinfo.get("value"))
            # 执行sql语句
            print(sqlStr)
            cursor.execute(sqlStr)
    # except:
    # 如果发生错误则回滚
    # db.rollback()
    # 提交到数据库执行
    db.commit()
    cursor.close()
    # 关闭数据库连接
    db.close()

url = 'http://fund.eastmoney.com/trade/hh.html?spm=001.1.swh'
os.makedirs('eastmoney',exist_ok=True)
# while not url.endswith('#'):
print('Downloading page %s' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
comicElem = soup.select('#tblite_hh > tbody > tr')
if comicElem == []:
    print('not found')
else:
    fundlist = []
    for tr in range(len(comicElem)):
        tdcomicElem = comicElem[tr].select('td')
        tdValue = comicElem[tr].select('td:nth-of-type(3) > span.fb')
        tdDate = comicElem[tr].select('td:nth-of-type(3) > span.date')
        tdName = comicElem[tr].select('td.fname > a')
        print(tdValue[0].text)
        print(tdDate[0].text)
        print(str(bytes(tdcomicElem[0].text,"UTF-8")))
        print(tdName[0].text)
        print('------')
        fundlist.append({"date":tdDate[0].text, "fundcode":tdcomicElem[0].text, "rank":tr, "fundname":tdName[0].text,"value":tdValue[0].text})
    print(fundlist)
    saveDB(fundlist)
print('Done.')
