import re
import os
import requests
import urllib
import time


class Spider():

    def __init__(self):
        self.keyword = input('欢迎使用pixabay图片搜索下载器\n请输入搜索关键词(推荐输入英文)：')
        self.siteURL = 'http://pixabay.com/zh/photos/?image_type=&cat=&min_width=&min_height=&q=' + str(
            self.keyword) + '&order=popular'

        # 获取详情页源码

    def getSource(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
            'Cookie': 'anonymous_user_id=a32f8936429b492394d04f56b1a603d0; is_human=1; csrftoken=9fpgurso37sJFDlLY8EjYDs34a1FK8Mr; _sp_ses.aded=*; lang=zh; dwf_show_mdp_getty_brand_ad=False; dwf_show_canva_banner_ads=False; dwf_es_default_operator_or=True; dwf_homepage_music_theme_links=True; __cf_bm=bb1CGezquhouneh2dSeHSzH5QzZ8._SX88ppAFEQ5pU-1715857564-1.0.1.1-OG_k04ZbGB_G7DMRI5EygmcBmMTW9RO_amg14GSSzeb_TwFCZd69eOpB0muZOx5vz2aFZnibl6hEPv_ecseoNA; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+16+2024+19%3A06%3A04+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202401.2.0&isIABGlobal=false&hosts=&consentId=0256d516-7e5d-4761-b87e-f205263c951d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&browserGpcFlag=0; _sp_id.aded=b2ff7c0a-b7d3-4269-867e-e9cecf03a9cc.1706947072.2.1715857570.1706947082.5ed58d5d-b9ee-4971-8f00-7451bcaa6ee6.7423bde0-9a4c-4251-931c-e8ae51963097.64b4b4c1-3268-4612-9eec-b1dde6da511b.1715851696945.26'}
        result = requests.get(url,headers=headers).text
        print(result)
        return result

        # 获取图片页数

    def getPageNum(self):
        result = self.getSource(self.siteURL)
        pattern = re.compile('<input name="pagi.*?>.*?/ (.*?) .*?', re.S)
        items = re.search(pattern, result)
        print(items)
        # if items.group() >= str(1):
        #     print('\n这个关键词共有图片', items.group(1), '页')
        # else:
        #     print('\n哎呀，木有您想要的图片呢。。。')
        return items.group(1)

        # 匹配正则1

    def getItem1(self, url):
        result = self.getSource(url)
        pattern1 = re.compile('<img srcset="https://cdn.pixabay.com/photo(.*?)-(.*?)__340.*?', re.S)
        items = re.findall(pattern1, result)
        return items

        # 匹配正则2

    def getItem2(self, url):
        result = self.getSource(url)
        pattern2 = re.compile('data-lazy-srcset="https://cdn.pixabay.com/photo(.*?)-(.*?)__340.*?', re.S)
        items = re.findall(pattern2, result)
        return items

        # 保存图片入文件

    def saveImage(self, detailURL, name):
        picture = urllib.request.urlopen(detailURL)
        fileName = name + '.jpg'
        string = 'D:\Cloud\%s\%s' % (self.path, fileName)
        E = os.path.exists(string)
        if not E:
            f = open(string, 'wb')
            f.write(picture.read())
            f.close()
        else:
            print('图片已经存在，跳过！')
            return False

    def makeDir(self, path):
        self.path = path.strip()
        E = os.path.exists(os.path.join('D:\Cloud', self.path))
        if not E:
            os.makedirs(os.path.join('D:\Cloud', self.path))
            os.chdir(os.path.join('D:\Cloud', self.path))
            print('成功创建名为', self.path, '的文件夹')
            return self.path
        else:
            print('名为', self.path, '的文件夹已经存在...')
            return False

            # 对一页的操作

    def saveOnePage(self, url):
        i = 1
        items = self.getItem1(url)
        for item in items:
            detailURL = 'https://cdn.pixabay.com/photo' + str(item[0]) + '-' + str(item[1]) + '_960_720.jpg'
            print('\n', '正在下载并保存图片', i, detailURL)
            self.saveImage(detailURL, name='Num' + str(i))
            time.sleep(0.5)
            i += 1
        if i > 16:
            items = self.getItem2(url)
            i = 17
            for item in items:
                detailURL = 'https://cdn.pixabay.com/photo' + str(item[0]) + '-' + str(item[1]) + '_960_720.jpg'
                print('\n', '正在下载并保存图片', i, detailURL)
                self.saveImage(detailURL, name='Num' + str(i))
                time.sleep(0.5)
                i += 1

                # 对多页图片的操作

    def saveMorePage(self):
        numbers = self.getPageNum()
        Num = int(input('一页共100张图，\n请输入要下载的页数(默认页数大于等于1）：'))
        Start = int(input('请输入下载起始页数：'))
        if numbers >= str(1):
            for page in range(Start, Start + Num):
                if page == 1:
                    print('\n', '正在获取第1页的内容......')
                    self.url1 = self.siteURL
                    self.makeDir(path=self.keyword + 'page' + str(page))
                    self.saveOnePage(url=self.url1)
                else:
                    print('\n', '正在获取第', page, '页的内容')
                    self.url2 = 'https://pixabay.com/zh/photos/?orientation=&image_type=&cat=&colors=&q=' + str(
                        self.keyword) + '&order=popular&pagi=' + str(page)
                    self.makeDir(path=self.keyword + 'page' + str(page))
                    self.saveOnePage(url=self.url2)
        else:
            return False

        print('\n', '所有图片下载成功！')


if __name__ == '__main__':
    spider = Spider()
    spider.saveMorePage()