import hashlib
import json

import requests
import time

def md5(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

def get_reponse():
    keyword=input('请输入关键词：')

    # 'c559131cfaa00682d19c598b0e6aeca6&1729090119387&34839810&{"pageNumber":1,"keyword":"笔记本","fromFilter":false,"rowsPerPage":30,"sortValue":"","sortField":"","customDistance":"","gps":"","propValueStr":{},"customGps":""}'
    stamp='1729089037797'
    base_data={"pageNumber":1,"keyword":keyword,"fromFilter":'false',"rowsPerPage":30,"sortValue":"","sortField":"","customDistance":"","gps":"","propValueStr":{},"customGps":""}
    base_md5 = 'c559131cfaa00682d19c598b0e6aeca6'+'&'+stamp+'&34839810&'+json.dumps(base_data,separators=(',',':'),ensure_ascii=False)
    print(base_md5)
    signature = md5(base_md5)
    print(signature)

def num():
    url ='https://www.goofish.com/'
    headers='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
    cookies='mtop_partitioned_detect=1; _m_h5_tk=c559131cfaa00682d19c598b0e6aeca6_1729095899255; _m_h5_tk_enc=c16c377cb6fe0f69db7630f232bfa3af; cookie2=13da08271d5f7645f8ee5768447a0cd4; _samesite_flag_=true; t=a73d1ed69b0b83708f9b88cbe3c6c2af; _tb_token_=eb3350eb936e5; isg=BOfnylabTPHXNch9ZNB2aSPqdhuxbLtONHVW5rlUA3adqAdqwTxLniWryig2W5PG; tfstk=g-Ctp0ijhkqiiC3EgmwHnjDW1HzhDsQavG7SinxihMIduihisIAMhEtd4hxguOxjkHI2jdA1SSBAj9RDj1XGH9INPdjAuP8XcisvmO23ZN7wgIZkD7Vl7Txd0x59GmbC7BTptpFuZN7sGnubl7fGbUDXqnOXCK9QOH8rCITXGyKBkUkjfiObJyLvPxM65dNBREYDGnsXGyQIC5z2mAtoMtksxKnZt5lxM6L9B3CDvjhYoFp9VNtp8e5L1dK55Hhb4s0WynKFNk2d8gX1jeSYwkd5UMCvFIFt4FBCyBtMN53wV1YArtQ82mYFCGCBH644QwCvXL16p4GDOB8fcKBU2bY9s9pR6OzqANskXTONo4EGJLBpUe9IkAOGEaf2F1Nt4HvykMplBuhOVgShZ_3u30xJoAULJxk2CeJB3YgfPMWVoeKu-8Mq3peeJ34LJxk2Ce8pqy5-3xJLL'
    res = requests.post(url)
    print(res)
    # print(res.text)


if __name__ == '__main__':
    # get_reponse()
    num()