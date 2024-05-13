# 跳過SSL憑證
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
import bs4

#
def getData(url):
    request = req.Request(url, headers = {
        "cookie":"over18=1", # 18x cookie 
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36" # add Agent
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 2. Analysis data
    soup = bs4.BeautifulSoup(data, "html.parser")
    titles = soup.find_all("div", class_="title")
    dates = soup.find_all("div", class_="date")
    the_title = []    
    the_date = []
    require_data = []

    the_date_count = 0

    for title in titles:
        if title.a !=None:
            # print(title.a.string)
            require_data.append({"title": title.a.string, "date": dates[the_date_count].string})
            
            # the_title = the_title + [title.a.string]
            # the_date = the_date + [dates[the_date_count].string]
        the_date_count+=1

    # 3. capture lots pages of web
    nextLink=soup.find("a", string="‹ 上頁") # find the <a> tag with 上頁

    # 處理title跟date
    

    result_data = {
        "result":{
            "url":nextLink["href"],
            "require_data":require_data
            }}
    print("*****",result_data)

    return result_data
    # return [nextLink["href"],the_title,the_date]

