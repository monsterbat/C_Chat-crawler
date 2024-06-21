# 跳過SSL憑證
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
import urllib.error
import bs4
import time

def getData(url, retries=3, backoff_factor=0.3):
    for attempt in range(retries):
        try:
            request = req.Request(url, headers={
                "cookie": "over18=1",  # 18x cookie 
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"  # add Agent
            })
            with req.urlopen(request) as response:
                data = response.read().decode("utf-8")
            
            # 2. Analysis data
            soup = bs4.BeautifulSoup(data, "html.parser")
            titles = soup.find_all("div", class_="title")
            dates = soup.find_all("div", class_="date")
            require_data = []

            the_date_count = 0

            for title in titles:
                if title.a is not None:
                    require_data.append({"title": title.a.string, "date": dates[the_date_count].string})
                the_date_count += 1

            # 3. capture lots pages of web
            nextLink = soup.find("a", string="‹ 上頁")  # find the <a> tag with 上頁

            result_data = {
                "result": {
                    "url": nextLink["href"],
                    "require_data": require_data
                }
            }

            return result_data

        except urllib.error.HTTPError as e:
            if e.code == 520:
                time.sleep(backoff_factor * (2 ** attempt))
                continue
            else:
                raise
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
    raise Exception(f"Failed to retrieve data from {url} after {retries} attempts")