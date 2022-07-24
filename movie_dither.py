from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import requests
import datetime
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
path = "C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path ,options=options)

time = datetime.datetime.now()
time = time.strftime('%Y/%m/%d/ %H:%M:%S')
TOKEN = 'eGeHRQ6ZlYTtZswvueLXDd4t0IfLwxjtEKuJKYQi9JS'
api_url = 'https://notify-api.line.me/api/notify'
#時刻を送る内容の変数に設定
movie_list = []
Cinema = ""
Moviename = ""

Moviename = input("調べたい映画の名前を入力してね")
Cinema = input("調べたい映画館の名前を入力してね")
send_contents = Moviename + "はないよ"

driver.get("https://www.aeoncinema.com/store/advance.html")
a = driver.find_element_by_xpath("//ul[@class='clearfix']/li/a[text()=\'"+Cinema+"\']")

driver.get(a.get_attribute("href"))
a = driver.find_elements_by_xpath("//ul/li/h3[@class='mql_pc_hide']/span")
for elements in a:
    movie_list.append(elements.get_attribute("textContent"))
    s = (elements.get_attribute("textContent"))
    if (Moviename in s):
        print(s)
        send_contents = Moviename + "前売り予約ができるよ"
print(movie_list)
if send_contents == Moviename + "はないよ":
    driver.get("https://www.aeoncinema.com/cinema2/all/movie/")
    a = driver.find_elements_by_xpath("//div[@class = 'cinemaBlockWrap']/div[@class='cinemaBlock clearfix enEven']/div[@class='cbCenterColumn']/p[@class='cbTitle']/a")
    for elements in a:
        s = (elements.get_attribute("textContent"))
        movie_list.append(s)
        print(movie_list)
        if (Moviename in s):
            print(s)
            send_contents = Moviename + "現在上映中"
            
    if send_contents == Moviename + "はないよ":
        driver.get("https://www.aeoncinema.com/cinema2/all/movie/comingsoon.html")
        a = driver.find_elements_by_xpath("//div[@class='cbCenterColumn']/p[@class='cbTitle']/a[text()=\'"+Moviename+"\']")
        print(a)
        for elements in a:
            s = (elements.get_attribute("textContent"))
            movie_list.append(s)
            print(movie_list)
            if (Moviename in s):
                print(s)
                send_contents = Moviename + "近日上映予定"
                a = driver.find_element_by_xpath("//div[@class='cbCenterColumn']/p[@class='cbTitle']/a[text()=\'"+Moviename+"\']")
                driver.get(a.get_attribute("href"))

TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}

image_file = './test.jpg'
binary = open(image_file, mode='rb')
image_dic = {'imageFile': binary}

requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)