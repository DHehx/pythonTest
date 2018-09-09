import requests,bs4,os
url = 'https://www.google.com/search?biw=1536&bih=758&tbm=isch&sa=1&ei=04WTW7TzDoPH8AP69pWYAg&q=monkey+d+luffy+gear+5&oq=monkey+d+luffy+gear+5&gs_l=img.3...18063.18232.0.18380.2.2.0.0.0.0.0.0..0.0....0...1c.1.64.img..2.0.0....0.K__5GxVVRLI'
os.makedirs('se',exist_ok=True)
while True:
    print('Downloading page %s' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,features="lxml")
    comicElem = soup.select('#ires > table > tr')
    if comicElem == []:
        print('not found')
    else:
        for tr in range(len(comicElem)):
            trcomicElem = comicElem[tr].select('td');
            for td in range(len(trcomicElem)):
                print(trcomicElem[td])
                a = trcomicElem[td].select('a > img')
                hSRGPdurl = a[0].get('src')
                print('DownLoading image %s...' % (hSRGPdurl))
                res = requests.get(hSRGPdurl)
                res.raise_for_status()
                # soup = bs4.BeautifulSoup(res.text, features="lxml")
                # purl = soup.select('#irc_cc > div:nth-child(2) > div.irc_t.i30052 > div.irc_mic > div.irc_mimg.irc_hic > a > img')
                imageFile = open(os.path.join('se', os.path.basename(str(tr) + '_' + str(td) +'.png')), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()