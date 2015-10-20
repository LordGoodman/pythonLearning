import urllib.request,os,http.cookiejar,shutil#用于删除非空目录
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
    soup=BeautifulSoup(read,"html.parser")
    return soup

def Download_opreate(dis):
        if(dis.find("\\")):
           dis=dis.replace("\\","")
        if(dis.find("*")):
           dis=dis.replace("*","")
        if(dis.find("?")):
           dis= dis.replace("?","")
        if(dis.find("/")):
           dis= dis.replace("/","")
        if(dis.find('"')):
           dis= dis.replace('"',"")
        if(dis.find("<")):
           dis= dis.replace("<","")
        if(dis.find(">")):
           dis= dis.replace(">","")
        if(dis.find("|")):
           dis= dis.replace("|","")

        return dis
        #path=r"F:\youmin"#定义文件夹路径
   # try: try 了之后特别慢...don't know why yet
    #    with open(path+'\\'+dis,"wb") as f:
   #        f.write(img)
    #        f.close()

    #except OSError:
      
      
def recursion_prase_img(url,path):
    first_connect=url_connect(url)
    first_soup=BeautifulCreat(first_connect)

    img=first_soup.find_all("img")
    for i in img :
        if i.find("br"):
            print(i.find("br").contents[0])
            form_temp=i['src'].rsplit(".")
            form=form_temp[len(form_temp)-1]
            full_path=i.find("br").contents[0].replace("\n","")+"."+form
            Download_opreate(full_path)
            try:
                f=open(path+"/"+full_path,"wb")#open后面要跟着文件名字！！！
                f.write(url_connect(i["src"]))
                f.close()
            except :
                pass
    for a in first_soup.find_all("a"):
        if a.get_text()==u"下一页" :
            recursion_prase_img(a["href"],path)

def recursion_prase_dir(soup):
    first=soup.find_all("a",{"class":"nrlj"})
    for i in range(10,20):
        print("***"+first[i]["title"],i)
   # for f in first:
    #    print("***",f["title"])
        name =first[i]["title"]
        name_re=Download_opreate(name)
        path="F:/youmin/"+name_re#不能有中文目录
        try:
            os.mkdir(path)
        except :
            shutil.rmtree(path)
            os.mkdir(path)
         
        recursion_prase_img(first[i]["href"],path)
        
    for a in soup.find_all("a"):
        if(a.get_text()==u">"):
           url_new=url_connect("http://so.gamersky.com/"+a["href"])
           soup_new=BeautifulCreat(url_new)
           recursion_prase_dir(soup_new)
            
if __name__=="__main__":
    req=url_connect("http://so.gamersky.com/?s=%u52a8%u6001%u56fe&node=20&p=3")
    soup=BeautifulCreat(req)
    
    recursion_prase_dir(soup)  


   
