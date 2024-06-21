## PTT Crawler
To find out which works are the most popular and discussed recently.

Current progress:
    Enter the category or keywords to search for the number of posts, then specify the search date to see how many articles appear.

利用空白鍵分隔不同的關鍵字
改成excel較易理解 
比較多個作品，並列出其數量

改成網頁形式

Bug
跨年處理
當下年份如何確定
點進去抓日期

# data form
data_result = {
    "result":{
        "url":link,
        "require_data":[
            {"title": title.a.string, "date": dates.string},
            ...
        ]
}}


