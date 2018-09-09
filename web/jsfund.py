#! python3
#嘉实基金基金信息爬取
import requests,os,bs4

url = 'http://www.jsfund.cn/izenportal/service/fundinfo/getBaseFundInfo?callback=jQuery112007047455902975863_1536496824527'
os.makedirs('jsfund',exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s' % url)
    res = requests.post(url,'{"fundcode": "004477"}')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#hot_004477')
    if comicElem == []:
        print('not found')
    else:
        comicUrl = url + comicElem[0].get('srcset')

        print('DownLoading image %s...' % (comicUrl))
        res = requests.get(comicUrl[:-3])
        res.raise_for_status()

        imageFile = open(os.path.join('xkcdNew',os.path.basename(comicUrl[:-3])),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    precLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + precLink.get('href')

print('Done.')
