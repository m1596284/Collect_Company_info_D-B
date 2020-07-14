import os
import requests
from time import sleep
import time
import datetime
import threading
from stem import Signal
from stem.control import Controller
import random
tStart = time.time()

pyPath = os.path.dirname(os.path.abspath(__file__)) #同上
f = open(pyPath +  '/catgory_till_company_urls_temp.txt',"r", encoding='UTF-8')
company_urls = f.readlines()
f.close
f = open(pyPath +  '/stop_point.txt',"r", encoding='UTF-8')
stop_points = f.readlines()
f.close
stop_point = stop_points[0].replace('\n','')
company_urls = company_urls[0:int(stop_point)]
session = requests.session()
session.proxies = {}
session.proxies['http']='socks5h://localhost:9050'
session.proxies['https']='socks5h://localhost:9050'
headerPara = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
Main_url = "https://www.dnb.com"
def job(ix,bot_num):
    f = open(pyPath +  '/test.txt',"r", encoding='UTF-8')
    company_urls = f.readlines()
    f.close
    for ixxx in range(0,int(len(company_urls)/bot_num)):
        print(company_urls[ixxx*bot_num+ix].replace('\n',''))
def renew_tor_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def job2(ix,bot_num,stop_url):
    ## Run final pages
    while len(company_urls) != 0:
        if stop_url == "":
            company_url = company_urls.pop().strip('\n')
            stop_url = company_url
        else:
            company_url = stop_url
        try:
            big_cat = company_url.split('\t')[0]
            small_cat = company_url.split('\t')[1]
            country_name = company_url.split('\t')[3]
            company_location = company_url.split('\t')[5]
            company_revenue = company_url.split('\t')[6]
            company_url = company_url.split('\t')[7]
            company_url = Main_url + company_url
            # sleep(random.randint(1,3))
            r = session.get(company_url, headers=headerPara)
            if r.text.find("You don't have permission to access") != -1:
                if ix < 10:
                    session.proxies = {}
                    session.proxies['http']='socks5h://localhost:9050'
                    session.proxies['https']='socks5h://localhost:9050'
                    renew_tor_ip()
                    r = session.get('http://icanhazip.com/')
                    print("Bot Num : " + str(ix) + " " + '\t' + str(datetime.datetime.now()) + " Renew IP address as : " + r.text.replace('\n',''))
            else:
                if  r.text.find('<h1 class="title">') != -1:
                    company_name = r.text[r.text.find('<h1 class="title">')+18:r.text.find('</h1>',r.text.find('<h1 class="title">')+18)]
                else:
                    company_name = "No company_name"
                if  r.text.find('<div class="tradeName">') != -1:
                    company_short_name = r.text[r.text.find('<div class="tradeName">')+23:r.text.find('</div>',r.text.find('<div class="tradeName">')+23)]
                else:
                    company_short_name = "No company_short_name"
                if  r.text.find('<div class="street_address_1">') != -1:
                    company_street_address1 = r.text[r.text.find('<div class="street_address_1">')+30:r.text.find('</div>',r.text.find('<div class="street_address_1">')+30)].replace(' ','').replace('\n','')
                else:
                    company_street_address1 = "No company_street_address1"
                if  r.text.find('<div class="street_address_2">') != -1:
                    company_street_address2 = r.text[r.text.find('<div class="street_address_2">')+30:r.text.find('</div>',r.text.find('<div class="street_address_2">')+30)].replace(' ','').replace('\n','')
                else:
                    company_street_address2 = ""
                if  r.text.find('<span class="company_postal">') != -1:
                    company_postal = r.text[r.text.find('<span class="company_postal">')+29:r.text.find('</span>',r.text.find('<span class="company_postal">')+29)].replace(' ','').replace('\n','')
                else:
                    company_postal = "No company_postal"
                if  r.text.find('<span class="company_region">') != -1:
                    company_region = r.text[r.text.find('<span class="company_region">')+29:r.text.find('</span>',r.text.find('<span class="company_region">')+29)]
                else:
                    company_region = "No company_region"
                if  r.text.find('<span class="company_country">') != -1:
                    company_country = r.text[r.text.find('<span class="company_country">')+30:r.text.find('</span>',r.text.find('<span class="company_country">')+30)]
                else:
                    company_country = "No company_country"
                if  r.text.find('<div class="phone">') != -1:
                    company_phone = r.text[r.text.find('<div class="phone">')+19:r.text.find('</div>',r.text.find('<div class="phone">')+19)].replace(' ','').replace('\n','')
                else:
                    company_phone = "No company_phone"
                if  r.text.find('<a href="http://') != -1:
                    company_web = r.text[r.text.find('<a href="http://')+9:r.text.find("target",r.text.find('<a href="http://')+9)-2]
                else:
                    company_web = "No company_web"
                if  r.text.find('<span class="type">') != -1:
                    company_type = r.text[r.text.find('<span class="type">')+19:r.text.find("</span>",r.text.find('<span class="type">')+19)].replace('&nbsp;',' ')
                else:
                    company_type = "No company_type"
                if  r.text.find('<span class="role">') != -1:
                    company_role = r.text[r.text.find('<span class="role">')+19:r.text.find("</span>",r.text.find('<span class="role">')+19)]
                else:
                    company_role = "No company_role"
                print("Bot Num : " + str(ix) + " " + '\t' + str(datetime.datetime.now()) + '\t' + " at : " + str(int(len(company_urls))) + " " + '\t' + big_cat  + '\t' + company_name)
                # print(company_name)
                # print(company_street_address1)
                # print(company_postal)
                # print(company_region)
                # print(company_country)
                # print(company_phone)
                # print(company_web)
                # print(company_type)
                # print(company_role)
                if company_street_address2 == "":
                    company_info = big_cat + '\t' + small_cat + '\t' +  company_name + '\t' + company_short_name + '\t' + country_name + '\t' + company_location + '\t' + company_revenue + '\t' + company_type + ' ' + company_role + '\t' + company_web + '\t' + company_street_address1.replace(", ",",").strip(",").replace(",",", ") + ", " + company_postal.replace(", ",",").strip(",").replace(",",", ") + ", " + company_region.replace(", ",",").strip(",").replace(",",", ") + ", " + country_name + '\t' + company_phone + '\t' + company_url
                else:
                    company_info = big_cat + '\t' + small_cat + '\t' +  company_name + '\t' + company_short_name + '\t' + country_name + '\t' + company_location + '\t' + company_revenue + '\t' + company_type + ' ' + company_role + '\t' + company_web + '\t' + company_street_address1.replace(", ",",").strip(",").replace(",",", ") + ", "  + company_street_address2.replace(", ",",").strip(",").replace(",",", ") + ", " + company_postal.replace(", ",",").strip(",").replace(",",", ") + ", " + company_region.replace(", ",",").strip(",").replace(",",", ") + ", " + country_name + '\t' + company_phone + '\t' + company_url
                # print(company_info)
                f = open(pyPath + "/company_information.txt","a", encoding='UTF-8') 
                f.write(company_info + '\n')
                f.close
                stop_url = ""
                f2 = open(pyPath +  '/stop_point.txt',"w", encoding='UTF-8')
                f2.write(str(int(len(company_urls))))
                f2.close
        except:
            job2(ix,bot_num,stop_url)
    tEnd = time.time()
    print("Spend: " + str(tEnd-tStart))
def thread_checker(checker_time,init_threads):
    while True:
        now_threads=[]#用来保存当前线程名称
        now = threading.enumerate()#获取当前线程名
        for i in now:
            now_threads.append(i.getName())#保存当前线程名称
        for init_thread in init_threads:
            if  init_thread in now_threads:
                pass #当前某线程名包含在初始化线程组中，可以认为线程仍在运行
            else:
                print('=== Thread : ' + init_thread,' stopped，now restart')
                ix = int(init_thread)
                bot_num = 10
                stop_url = ""
                t = threading.Thread(target = job2, args = (ix,bot_num,stop_url))#重启线程
                t.setName(str(ix))#重设name
                t.start()
        sleep(checker_time)#隔一段时间重新运行，检测有没有线程down

threads = []
init_threads = []
bot_num = 10
checker_time = 60
for ix in range(bot_num):
    stop_url=""
    t = threading.Thread(target = job2, args = (ix,bot_num,stop_url))
    t.setName(str(ix))
    init_threads.append(str(ix))
    threads.append(t)
    threads[ix].start()
checker = threading.Thread(target=thread_checker,args=(checker_time,init_threads))
checker.start()

for iix in range(bot_num):
    threads[iix].join()