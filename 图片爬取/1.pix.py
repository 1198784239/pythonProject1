import time

import parsel
import requests
import re
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
            'Cookie':
"anonymous_user_id=a32f8936429b492394d04f56b1a603d0; is_human=1; csrftoken=9fpgurso37sJFDlLY8EjYDs34a1FK8Mr; _sp_ses.aded=*; lang=zh; dwf_show_mdp_getty_brand_ad=False; dwf_show_canva_banner_ads=False; dwf_es_default_operator_or=True; dwf_homepage_music_theme_links=True; client_width=2754; __cf_bm=3qEigRrOcbp3jkb7ny3tDR6rP7TKvZJxi5O4smJq3F0-1715863088-1.0.1.1-qB5CU3K.xgQrW6GDkm6sAsp_ooXCkUCqLkt2jr1pxy8Zi857v5lF3.3nRFV9cwfiG2ZB4ZFZJ_YRuD0EmD12bQ; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+16+2024+20%3A38%3A28+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202401.2.0&isIABGlobal=false&hosts=&consentId=0256d516-7e5d-4761-b87e-f205263c951d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&browserGpcFlag=0; _sp_id.aded=b2ff7c0a-b7d3-4269-867e-e9cecf03a9cc.1706947072.2.1715863114.1706947082.5ed58d5d-b9ee-4971-8f00-7451bcaa6ee6.7423bde0-9a4c-4251-931c-e8ae51963097.64b4b4c1-3268-4612-9eec-b1dde6da511b.1715851696945.58"}
url = 'https://pixabay.com/zh/photos/'
try:
    res = requests.get(url,headers=headers).text
    # print(res)

    Pa = parsel.Selector(res,'html')
    Data =Pa.xpath('//*[@id="app"]/div[1]/div[2]/div[1]').get()
    # print(Data)
    src = re.compile('class="link--WHWzm" href="(.*?)"',re.S)
    m =re.findall(src,str(Data))
    print(m)
    for i in range(len(m)):
        url ='https://pixabay.com/'+m[i]
        print(url)
        aa= requests.get(url,headers=headers).text
        Pa1 = parsel.Selector(aa,'html')
        # print(Pa1)
        SRC =Pa1.xpath('//*[@id="app"]/div[1]/div/div/div[1]/div[1]/div/div/img/@src').get()
        print(SRC)
        requ = requests.get(SRC,headers=headers).content
        with open('壁纸'+str(i)+'.jpg',mode='wb')as f:
            f.write(requ)
except requests.exceptions.ConnectionError:
    res.status_code = "Connection refused"



