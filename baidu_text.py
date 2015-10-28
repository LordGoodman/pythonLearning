import urllib.request,http.cookiejar
from bs4 import BeautifulSoup

def url_connect(url):

        
    cj = http.cookiejar.CookieJar()
    cookieproc=urllib.request.HTTPCookieProcessor(cj)
    opener=urllib.request.build_opener(cookieproc)
    req=urllib.request.Request(url)
    req.addheaders = [('User-Agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36")]
    try:
        respond=urllib.request.urlopen(req)
    except : 
        pass
        #http.cookiejar.CookieJar.clear(self)
        #url_connect(url)
    return respond.read()

def BeautifulCreat(read):
    soup = BeautifulSoup(read,"html.parser")
    return soup

def prase_url(soup):
    items = soup.find_all("h3")
    next_page="下一页>".encode("utf8")
    #print(soup.prettify())
    for item in items:
        a=item.find("a")
        print(a.get_text())
        print(a["href"])
        print("---------------------------------")

    next_page_a=soup.find("a", string=next_page)
    try:
        respone=url_connect("http://www.baidu.com"+next_page_a["href"])
        soup_next=BeautifulCreat(respone)
        prase_url(soup_next)
    except:
        pass
if __name__ == '__main__':
    keyword = "bilibili"#这里输入你的英文关键字
    url= 'http://www.baidu.com/s?wd=%s&rsv_bp=0&rsv_spt=3&rsv_n=2&inputT=6391'%keyword.encode("utf8")
    connect = url_connect(url)
    soup = BeautifulCreat(connect)
    prase_url(soup)
