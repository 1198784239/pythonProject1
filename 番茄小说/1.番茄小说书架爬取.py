import time
from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def get_html():
    Data = []
    for page in range(1, 6):
        driver.get(f"https://fanqienovel.com/library/all/page_{page}?sort=hottes")
        time.sleep(2)
        html = driver.page_source
        Html = etree.HTML(html)
        with ThreadPoolExecutor(max_workers=10) as executor:
            for num in range(1, 19):
                # partt = re.compile(r'\\\w{5}',re.S)
                src = Html.xpath(f'//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div{[num]}/div/div[1]/div/img/@src')
                titles = Html.xpath(f'//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div{[num]}/div/div[2]/div[1]/a/text()')
                aurth = Html.xpath(
                    f'//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div{[num]}/div/div[2]/div[2]/span/span/text()')
                times = Html.xpath(f'//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div{[num]}/div/div[2]/div[5]/span/text()')
                Src = src[0]
                Title = titles[0]
                Aurth = aurth[0]
                Time = times[0]
                Data.append([Src, Title, Aurth, Time])
                executor.submit(down_img, Src,titles)
        time.sleep(1)
    print(Data)
    return Src,titles
    # print(Src)
    # print(Data)
    # print(Data)
    # tielec = re.sub(partt,'',titles).strip()
    # Aurth = re.sub(partt,'',aurth).strip()
def down_img(Scr,titles):
    # for i in range(100):
    #     url = Data[i][0]
    #     til = Data[i][1]
    img = requests.get(Scr,verify=False)
    with open(f'img/{titles[0]}.jpg', 'wb') as f:
        f.write(img.content)
        print(titles,'写入成功')


if __name__ == '__main__':
    HTML = get_html()
    down_img(HTML[0],HTML[1])
