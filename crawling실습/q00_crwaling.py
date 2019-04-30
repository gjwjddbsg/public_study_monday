from bs4 import BeautifulSoup as BS
import gevent.pool
import requests
pool = gevent.pool.Pool(10)
def main():
    headers = { 'User-Agent': 'Mozilla/5.0' }
    get_data = requests.get('https://www.naver.com',headers=headers)
    soup = BS(get_data.text,'html.parser')
    crurl = soup.select(
            '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li'
           )
    keyworkd = []
    def getRelated(keyword):
        headers = { 'accept': '*/*','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'}
        get_data = requests.get(keyword[2],headers=headers)
        soup = BS(get_data.text,'html.parser')
        rval= soup.select('#nx_related_keywords > dl > dd.lst_relate._related_keyword_list > ul > li > a')
        keyword.append([ a.text for a in rval])


    for i,v in enumerate(crurl):
        subkeyworkd=[]
        subkeyworkd.append(v.find('span',{'class':'ah_r'}).text)
        subkeyworkd.append(v.find('span',{'class':'ah_k'}).text)
        subkeyworkd.append(v.find('a').get('href'))
        
        keyworkd.append(subkeyworkd)
    pool.map(getRelated, keyworkd)
    
    for a in keyworkd:
        print(a[0])
        print(a[1])
        print(a[3])
main()
