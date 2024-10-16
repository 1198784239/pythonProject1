import requests
import hashlib
# eE(em.token + "&" + eC + "&" + eS + "&" + ep.data)

em_token='258fc89bf67b5944b0de832b3ceb0274'
eC=1729093980858
eS='12574478'
ep_data='{"appId":"34385","params":"{\"device\":\"HMA-AL00\",\"isBeta\":\"false\",\"grayHair\":\"false\",\"from\":\"nt_history\",\"brand\":\"HUAWEI\",\"info\":\"wifi\",\"index\":\"4\",\"rainbow\":\"\",\"schemaType\":\"auction\",\"elderHome\":\"false\",\"isEnterSrpSearch\":\"true\",\"newSearch\":\"false\",\"network\":\"wifi\",\"subtype\":\"\",\"hasPreposeFilter\":\"false\",\"prepositionVersion\":\"v2\",\"client_os\":\"Android\",\"gpsEnabled\":\"false\",\"searchDoorFrom\":\"srp\",\"debug_rerankNewOpenCard\":\"false\",\"homePageVersion\":\"v7\",\"searchElderHomeOpen\":\"false\",\"search_action\":\"initiative\",\"sugg\":\"_4_1\",\"sversion\":\"13.6\",\"style\":\"list\",\"ttid\":\"600000@taobao_pc_10.7.0\",\"needTabs\":\"true\",\"areaCode\":\"CN\",\"vm\":\"nw\",\"countryNum\":\"156\",\"m\":\"pc\",\"page\":3,\"n\":48,\"q\":\"%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91\",\"qSource\":\"url\",\"pageSource\":\"a21bo.jianhua/a.201867-main.d1_2_1.5af92a89N9nvNJ\",\"tab\":\"all\",\"pageSize\":\"48\",\"totalPage\":\"42\",\"totalResults\":\"2000\",\"sourceS\":\"48\",\"sort\":\"_coefp\",\"bcoffset\":\"-22\",\"ntoffset\":\"2\",\"filterTag\":\"\",\"service\":\"\",\"prop\":\"\",\"loc\":\"\",\"start_price\":null,\"end_price\":null,\"startPrice\":null,\"endPrice\":null,\"categoryp\":\"\",\"myCNA\":\"+ITtGm6OhksCAdzN4bGeuS4n\"}"}'
string = em_token +"&"+ str(eC) +"&" + eS + "&" + ep_data
MD5 =hashlib.md5()
MD5.update(string.encode('utf-8'))
sign = MD5.hexdigest()
print(sign)