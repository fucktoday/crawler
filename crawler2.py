# coding: utf-8 

from bs4 import BeautifulSoup
import requests
import codecs
import time
import random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Pragma':'no-cache',
        'Referer':'www.baidu.com'
        }

headers2 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie':'lianjia_uuid=ca66040e-ae60-477c-870c-aef58e41b74b; gr_user_id=d16fa75d-016d-4a3b-ad46-b83c725b8177; pt_393d1d99=uid=R6ox6usBIw8oijc4-jdg1A&nid=0&vid=QjI/ALyvPnjCgzD6wKp02A&vn=4&pvn=5&sact=1486889618895&to_flag=0&pl=33w-jdLFFqzPJb31BoS3kQ*pt*1486889530530; cityCode=sh; ubt_load_interval_b=1494584719915; ubta=2299869246.1906553635.1473232189094.1494584658842.1494584720430.616; ubtc=2299869246.1906553635.1494584720432.D4E4DE9E37BC831EA195F72CE192A4A9; ubtd=5; all-lj=5ce010dbdb86da2c0bba3b0cda32eb3e; UM_distinctid=15bfca39a8024d-0207404fd782ae-30627509-1aeaa0-15bfca39a815c; sample_traffic_test=test_66; select_city=110000; _smt_uid=58b984f1.38c6ab7b; CNZZDATA1253477573=1199994947-1494587665-%7C1495035106; CNZZDATA1254525948=77215090-1494588843-%7C1495032114; CNZZDATA1255633284=406639099-1494587847-%7C1495034007; CNZZDATA1255604082=2083075898-1494586833-%7C1495034216; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _ga=GA1.2.384124637.1473232188; _gid=GA1.2.680613954.1495037341; _gat_dianpu_agent=1; lianjia_ssid=d13cb476-bad1-4105-abee-88775d86de56',
        'Host':'bj.lianjia.com',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

headers3 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie':'lianjia_uuid=ca66040e-ae60-477c-870c-aef58e41b74b; gr_user_id=d16fa75d-016d-4a3b-ad46-b83c725b8177; pt_393d1d99=uid=R6ox6usBIw8oijc4-jdg1A&nid=0&vid=QjI/ALyvPnjCgzD6wKp02A&vn=4&pvn=5&sact=1486889618895&to_flag=0&pl=33w-jdLFFqzPJb31BoS3kQ*pt*1486889530530; cityCode=sh; ubt_load_interval_b=1494584719915; ubta=2299869246.1906553635.1473232189094.1494584658842.1494584720430.616; ubtc=2299869246.1906553635.1494584720432.D4E4DE9E37BC831EA195F72CE192A4A9; ubtd=5; all-lj=5ce010dbdb86da2c0bba3b0cda32eb3e; UM_distinctid=15bfca39a8024d-0207404fd782ae-30627509-1aeaa0-15bfca39a815c; sample_traffic_test=test_66; select_city=110000; _smt_uid=58b984f1.38c6ab7b; CNZZDATA1253477573=1199994947-1494587665-%7C1495035106; CNZZDATA1254525948=77215090-1494588843-%7C1495032114; CNZZDATA1255633284=406639099-1494587847-%7C1495034007; CNZZDATA1255604082=2083075898-1494586833-%7C1495034216; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _ga=GA1.2.384124637.1473232188; _gid=GA1.2.680613954.1495037341; _gat_dianpu_agent=1; lianjia_ssid=d13cb476-bad1-4105-abee-88775d86de56',
        'Host':'bj.lianjia.com',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30'
        }

headers_list = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
        {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
        {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
        {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
        {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
        {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
        {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
        {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
        {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
        {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
        {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]

def getUrls(name):
    start = time.time()
    outputFp = codecs.open('urls_%s.txt' % (name), 'w', 'utf-8')
    for i in xrange(1, 100):
        url = 'http://bj.lianjia.com/chengjiao/pg%drs%s/' % (i, name)
        try:
            #response = requests.get(url, headers = headers_list[random.randint(0,len(headers_list)-1)], timeout = 10)
            response = requests.get(url, headers = headers2, timeout = 10)
        except Exception, e:
            print e
            continue
        if response.status_code != 200:
            print "list page: %d request error, erro code: %d" % (i, response.status_code)
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        listContent = soup.find_all(class_='listContent')
        if len(listContent) == 0:
            print "list page: " + str(i) + " can't find listContent tag"
            continue
        for j in xrange(len(listContent[0])):
            detailUrl = listContent[0].contents[j].contents[0].attrs['href']
            outputFp.write(detailUrl + "\n")

        if i % 10 == 0:
            end = time.time()
            print "urls page num %d:, cost %d seconds" % (i, end - start)
        time.sleep(random.randint(1, 3))
    outputFp.flush()
    outputFp.close()
    end = time.time()
    print "getUrl cost time: %d seconds" % (end - start)
        
def getInfo(name):
    start = time.time()
    lineNum = 1
    inputFp = codecs.open('urls_%s.txt' % (name), 'r', 'utf-8')
    infoFp = codecs.open('info_%s.txt' % (name), 'w', 'utf-8')
    for url in inputFp.readlines():
        #get web html
        try:
            #response = requests.get(url.strip(), headers = headers_list[random.randint(0,len(headers_list)-1)], timeout = 5)
            response = requests.get(url.strip(), headers = headers2, timeout = 5)
        except Exception, e:
            print e
            continue
        if response.status_code != 200:
            print "info page: %s request error, erro code: %d" % (url.strip(), response.status_code)
            continue
        soup = BeautifulSoup(response.text, 'lxml')

        #parse rightup info
        result = soup.find_all(class_="info fr")
        if len(result) == 0:
            print "info page can't find rightup info_fr tag. url: %s" % (url.strip())
            continue
        if len(result) > 1:
            print "info page info_fr tag find result > 1. url: %s" % (url.strip())
            continue
        for div in result[0].contents:
            if div['class'] == "msg":
                for span in div.contents:
                    infoFp.write(span.contents[0].string + "\t")
                break
            else:
                continue

        #parse middle info
        result = soup.find_all(class_="base")
        if len(result) == 0:
            print "info page can't find middle base tag. url: %s" % (url.strip())
            continue
        if len(result) > 1:
            print "info page middle base tag find result > 1. url: %s" % (url.strip())
            continue
        for info in result[0].contents[1].contents[0].contents:
            infoFp.write(info.contents[1].string.strip() + "\t")
        result = soup.find_all(class_="transaction")
        if len(result) == 0:
            print "info page can't find middle transaction tag. url: %s" % (url.strip())
            continue
        if len(result) > 1:
            print "info page middle transaction tag find result > 1. url: %s" % (url.strip())
            continue
        for info in result[0].contents[1].contents[0].contents:
            infoFp.write(info.contents[1].string.strip() + "\t")

        #parse down info
        result = soup.find_all(class_="record_price")
        if len(result) == 0:
            print "info page can't find down record price tag. url: %s" % (url.strip())
            continue
        for index in xrange(len(result)):
            #infoFp.write(result[index].string.strip() + str(index+1) + "\t")
            infoFp.write(result[index].string.strip() + "\t")
        result = soup.find_all(class_="record_detail")
        if len(result) == 0:
            print "info page can't find down record detail tag. url: %s" % (url.strip())
            continue
        for index in xrange(len(result)):
            #infoFp.write(result[index].string.strip() + str(index+1) + "\t")
            infoFp.write(result[index].string.strip() + "\t")

        infoFp.write("\n")

        if lineNum % 10 == 0:
            end = time.time()
            print "info page num %d:, cost %d seconds" % (lineNum, end - start)
        lineNum += 1
        time.sleep(random.randint(1, 3))

    infoFp.flush()
    infoFp.close()
    inputFp.close()


if __name__ == "__main__":
    #getUrls(sys.argv[1])
    getInfo(sys.argv[1])

