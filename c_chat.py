"""
Crawler C_Chat
Latest:2024/05/12
"""
# 
from basic_function import getData as getData
from datetime import datetime

def c_chat_z(keyword, date, search_type):
    pageurl="https://www.ptt.cc/bbs/LoL/index.html"
    keyword_count = 0
    keyword = keyword.lower()
    title_total=[]
    title_total_lower = []
    date_total = []
    keyword_length = len(keyword)

    # Creat file and clean previous data
    with open("PTT LoL list.txt", "w",encoding="utf-8",newline='') as data_result_01:
        data_result_01.write("")

    # Choose data need analysis
    # 輸入日期
    date_year = int(date.split("/")[0])
    date_month = int(date.split("/")[1])
    date_day = int(date.split("/")[2])
    # 當下日期
    now = datetime.now()
    now_year = int(now.year)
    now_month = int(now.month)
    now_day = int(now.day)

    switch = True

    while switch == True:
        # 
        data_result = getData(pageurl)
        # 取出日期驗證
        page_date = data_result["result"]["require_data"][0]["date"]
        now = datetime.now()
        now_year = int(now.year)

        page_year = int(now_year)
        page_month = int(page_date.split("/")[0])
        page_day = int(page_date.split("/")[1])

        print("---1---",switch)
        if date_year > page_year:
            switch = False
            print("---1.1---",switch,date_year,page_year)
        if date_year == page_year:
            if date_month > page_month:
                switch = False
                print("---1.2---",switch,date_month,page_month)
            if date_month == page_month:
                if date_day > page_day:
                    switch = False
                    print("---1.3---",switch,date_day,page_day)
        print("---2---",switch,"page_day",page_day,"  date_day",date_day)
        if switch == True:
            
            require_data_result = data_result["result"]["require_data"]

            # title_total = title_total+getData(pageurl)[1]
            # title_total_lower = title_total_lower+[data_ls.lower() for data_ls in getData(pageurl)[1]]
            import_data(require_data_result,search_type,keyword_length,keyword)
        print("---3---",switch)

        pageurl="https://www.ptt.cc" + data_result["result"]["url"]#換頁




def import_data(require_data_result,search_type,keyword_length,keyword):    
    # Importing data
    # 變小寫
    require_data_result_lower = require_data_result
    for title_result_ls in require_data_result_lower:
        title_result_ls["title"] = title_result_ls['title'].lower()
    # 找標題
    print("---4---")
    if search_type == "title only":
        for require_data_result_lower_ls in require_data_result_lower:
            # print("!!!!!!!!",type(movie_title_filter))
            title_result_lower = require_data_result_lower_ls["title"]
            if title_result_lower[1:keyword_length+1] == keyword:
                with open("PTT LoL list.txt", "a",encoding="utf-8",newline='') as data_result_01:
                    data_result_01.write(str(title_result_lower))
                    data_result_01.write("\n")
    
    # 模糊搜尋         
    if search_type == "include all":  
        for require_data_result_lower_ls in require_data_result_lower:
            title_result_lower = require_data_result_lower_ls["title"]
            if keyword in title_result_lower:
                # print("*****",movie_title_filter_1)
                with open("PTT LoL list.txt", "a",encoding="utf-8",newline='') as data_result_01:
                    data_result_01.write(str(title_result_lower))
                    data_result_01.write("\n")

    print("Finish!")

def c_chat_z1(c1,c2):
      print(c1,"/",c2)