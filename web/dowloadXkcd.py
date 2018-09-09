#! python3
#下载网页图片
import requests,os,bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#comic img')
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
