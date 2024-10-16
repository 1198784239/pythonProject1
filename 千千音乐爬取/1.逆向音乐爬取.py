import os.path
import requests
from bs4 import BeautifulSoup
import hashlib
import time

def createSign(r):
    r1 = r+'0b50b02fd0d73a9c4c8c3a781c30845f'
    hash = hashlib.md5(r1.encode('utf-8')).hexdigest()
    return hash

# print(createSign('16073360','T10059607241','1718526002'))
words=input('请输入关键词:')
url = f'https://music.91q.com/search?word={words}'
res = requests.get(url)

BS = BeautifulSoup(res.text, 'html.parser')
page_tags = BS.find_all('li',class_='number')
total_pages = 0
if len(page_tags)==0:
    total_pages=1
else:
    total_pages = int(page_tags[-1].text)
# print(total_pages)
# title_boxs = BS.find_all('div', class_='song-box')
# sing_boxs = BS.find_all('div', class_='artist ellipsis')

for index in range(1,(total_pages)+1):
    word = words
    appid ='16073360'
    timestamp = str(int(time.time()))
    r = 'appid=16073360&pageNo=%s&pageSize=20&timestamp=%s&type=1&word=%s' % (index,timestamp,word)
    sign1 = createSign(r)
    params = {
        'sign':sign1,
        'appid':appid,
        'word':words,
        'type':'1',
        'timestamp':timestamp,
        'pageNo':str(index),
        'pageSize':20
    }
    pageres = requests.get('https://music.91q.com/v1/search?', params=params)
    song_info=pageres.json()
    # print(song_info)
    for track in song_info['data']['typeTrack']:
        # print(track)
        TSID = track['TSID']
        albumTitle = track['title']
        singer_name = ''
        for singer in track['artist']:
            singer_name += singer['name']
            singer_name = singer_name.replace(' ', '')
            # print(singer_name)
        r = 'TSID='+TSID+'&appid=16073360&timestamp='+timestamp
        sign = createSign(r)
        params = {
            'sign': sign,
            'appid': appid,
            'timestamp':timestamp,
            'TSID':TSID,
        }
        res1 = requests.get('https://music.91q.com/v1/song/tracklink?', params=params)
        info = res1.json()
        # print(info)
        if 'path' in info['data']:
            # print(info['data']['path'])
            song_name = info['data']['title']
            song_name = song_name.replace(' ','')
            print(song_name)
            response =requests.get(info['data']['path'])
            try:
                if not os.path.exists('./music'):
                    os.mkdir('./music')
                with open('./music/%s+%s.mp3' %(song_name,singer_name), 'wb') as f:
                    f.write(response.content)
                print('下载完毕')
            except:
                print('文件已存在')

    # print(song_info)
    # if 'path' in song_info['data']:
    #     # print(song_info['data']['path'])
    #     response = requests.get(song_info['data']['path'])
    #     song_name = song_info['data']['title']
    #     singer_name =''
    #     for singer in song_info['data']['artist']:
    #         singer_name += singer['name']+' '
    #     # print(singer_name)
    #     with open('./music/%s+%s.mp3' %(singer_name,song_name), 'wb') as f:
    #         f.write(response.content)



    # print(title_boxs[index].find('a').text)
    # print('https://music.91q.com'+title_boxs[index].find('a')['href'])
#
# for sings in range(0,len(sing_boxs)):
#     sing_name=''
#     for sing1 in sing_boxs[sings].find_all('a'):
#         sing_name += sing1.string +' '
#     print(sing_name)