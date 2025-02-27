import requests
import pprint
import re
from tqdm import tqdm

url ='https://vd6.l.qq.com/proxyhttp'
data ={"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc002000y0ehh8%2Fs4100gaakjh.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc002000y0ehh8%2Fs4100gaakjh.html&sphttps=1&encryptVer=9.2&cKey=qfa_Fg3Ulom1yM1Orq2-LnCjnpb8Ocr0cPTe1piKzEul_f4vOWcoV2JPcsrTrLY8PVNU1xVUzAJz_oLVGCTZlxo--_XGuZWLjvmpaTXWr2DNOLGAi4iBp92IyL4ip4GdgUquu4cL4cExCyKh6cqchEKDlC2uGzpCCamWfdlZnHB5x6wVJHKsVyf3svRoLvLp4yt5irIvBazTFI6klX7qSYlxDPbyyf8e8SL3SEnu3RmvgibC5O609WqcznaZw0af2pySApuO_cBm7THy64l64PYvrkyjWSbCwdTotxl9EsF2Jd-Rgt64sMmNnLeut5kJP7ANmOExsITvfbCpmYgjx7BF2Nn6b_9ZY6SvHftP2Mir5BxcNmENw_kHQy1AwwI8SecmJekIcokp25Ao9OEt0aG1fJHVqpK-6FPRhNoy34lI5tz8EgTEi-Lz4H77taVCIujr93auZpMARQkzoTXKzhxJpqzctF8XQIbpH9-9MIDbUuC0lJ6_WpxlWWOHeUlTCB_gZ2CQ559ml3Rcp1KlSS0-vRQ-G6v5ybnOAQQEBAQbcB6B&clip=4&guid=c55cb0844682cbba&flowid=09ca5e392cc1e55ed7a32330494555f3&platform=10201&sdtfrom=v1010&appVer=1.35.15&unid=&auth_from=&auth_ext=&vid=s4100gaakjh&defn=fhd&fhdswitch=0&dtype=3&spsrt=2&tm=1729254744&lang_code=0&logintoken=&spvvpay=1&spadseg=3&spvvc=3&spav1=15&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&hevclv=31&drm=296","sspAdParam":"{\"ad_scene\":1,\"pre_ad_params\":{\"ad_scene\":1,\"user_type\":0,\"video\":{\"base\":{\"vid\":\"s4100gaakjh\",\"cid\":\"mzc002000y0ehh8\"},\"is_live\":false,\"type_id\":2,\"referer\":\"https://v.qq.com/channel/choice\",\"url\":\"https://v.qq.com/x/cover/mzc002000y0ehh8/s4100gaakjh.html\",\"flow_id\":\"09ca5e392cc1e55ed7a32330494555f3\",\"refresh_id\":\"a36eadb9303fd67c9fca7e2a0fe41d34_1671341127\",\"fmt\":\"fhd\"},\"platform\":{\"guid\":\"c55cb0844682cbba\",\"channel_id\":0,\"site\":\"web\",\"platform\":\"in\",\"from\":0,\"device\":\"pc\",\"play_platform\":10201,\"pv_tag\":\"film_qq_com|channel\",\"support_click_scan_integration\":true},\"player\":{\"version\":\"1.35.13\",\"plugin\":\"4.1.9\",\"switch\":1,\"play_type\":\"0\"},\"token\":{\"type\":0,\"vuid\":0,\"vuser_session\":\"\",\"app_id\":\"\",\"open_id\":\"\",\"access_token\":\"\"},\"req_extra_info\":{\"now_timestamp_s\":1729254744,\"ad_frequency_control_time_list\":{}},\"extra_info\":{}}}","adparam":"adType=preAd&vid=s4100gaakjh&sspKey=nqwm"}
headers ={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
'Cookie' :'pac_uid=0_577eaf978fdaf; iip=0; tvfe_boss_uuid=65e003ec74ce56cb; pgv_pvid=8511518562; appuser=109C0D025A94DFDA; RK=O59dCiWkYR; ptcz=4a22a47fa9f6647c7290638766e0870e74a9a7abc5d07b1ef89b3d9af01f9e36; fqm_pvqid=9727c32c-66f1-4518-9479-2d1e8f3506c9; o_minduid=HWrWjMeRby3M1ZFuQIQ-axZAjTrthQiy; qq_domain_video_guid_verify=c55cb0844682cbba; _qimei_uuid42=17b03133521100e5084abee6083e435bf26b146bca; _qimei_q36=; _qimei_h38=90773195084abee6083e435b0200000b017b03; ETCI=bdfda4931c6f436fa3b744b82ec9f7e5; o_cookie=1198784239; ad_session_id=2qpkarxh5jguw; _qimei_fingerprint=942a76889b793eb0af6246554bfaa7d9; _clck=1h1syuo|1|fq1|0; pgv_info=ssid=s2557381428; vversion_name=8.2.95; video_omgid=c55cb0844682cbba; LZTturn=864; LZCturn=910; LPSJturn=924; LBSturn=113; LVINturn=370; LPHLSturn=237; Lturn=549; LKBturn=488; LPVLturn=982; LPLFturn=81; LDERturn=924'}
res = requests.post(url, json=data,headers=headers)
# print(res.json())
html_data = res.json()['vinfo']
# print(html_data)
html=re.findall(r'url(.*?),',html_data)[5]
html_new  =re.split(r'"',html)[2]
response = requests.get(html_new,headers=headers).text
response = re.sub(r'#EXTM3U','',response)
response = re.sub(r'#EXT-X-VERSION:\d','',response)
response = re.sub(r'#EXT-X-MEDIA-SEQUENCE:\d','',response)
response = re.sub(r'#EXT-X-TARGETDURATION:\d+','',response)
response = re.sub(r'#EXT-X-PLAYLIST-TYPE:VOD','',response)
response = re.sub(r'#EXT-X-ENDLIST','',response)
response = re.sub(r'#EXTINF:\d+\.\d+,','',response).split()
for i in tqdm(response):
    # print(i)
    i_url ='https://094f7c53507f6830ec416946a2760048.v.smtcdns.com/moviets.tc.qq.com/AloBGvC_BkrNVXPQfIpqzKSou9VITwJ_AISqcyjq2mEA/B_JxNyiJmktHRgresXhfyMetZl7kNIKsuyb5ECsGfrRfxqAshCoyyyoJB3pFgQnxgG/svp_50112/yorDvtYlHWmNrh_9VhgRmWMmW2G_q3KNXe-GSBqe0lvUa_AzstCzQhhEeV--QFOsA4WLLqGoBdgzuuUL4sNXti70M4akIp7E-7kdeAM20xaLxdli-PZr0JwWB-RmgQ8ex4PaB14zV8ItxOqxjLQl8SRTa_3J5QG2j2FUyDStkkeVpTAFlEpQKyKxuu3knwIpfhVvjmQVIOTeCT4kfpPYRQJgFxjr_MfjcVxbcJkVW69_ZHJYYqUHpw/'
    base  =i_url+i
    resp = requests.get(base).content
    with open('锦绣安宁.mp4',mode='ab') as f:
        f.write(resp)

print('下载完成')
