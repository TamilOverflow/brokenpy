import requests
from bs4 import BeautifulSoup
import sys

sm_sites_present =[]
founded_data={}

class BrokenLinkPy():

    def __init__(self):
        pass
    
    def crawl_req(self,get_target=[],gets_social=[]):
       print("\n[+]{} \n".format("crawler py Startting"))

       try:
           if len(get_target) < 1 :
                print("Data not found in <target>!")
                sys.exit()
           if len(gets_social) < 1 :
                print("Data not found in <social link provider>!")
                sys.exit()
           for i_data in get_target:
                target_url = i_data
                print("[+]=================================[{}]==============================".format(i_data))
                founded_data[i_data] =[]
                with requests.Session() as s:
                    s.headers={"User-Agent":"Mozilla/5.0"}
                    s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
                    req = s.get(target_url)
                    soup = BeautifulSoup(req.content, 'html5lib')
                all_links = soup.find_all('a', href = True)
                for link in all_links:
                    founded_data[i_data].append(link.attrs['href'])
                    #print(link.attrs['href'])
                    # if "facebook.com" in link.attrs['href']:
                    #     print(link.attrs['href'])
                if len(founded_data[i_data]) <1:
                    print("[-] no data found!")
                    print("[+]======================================================================================== \n")
                else:
                    for ss_data in gets_social:
                        #print(ss_data)
                        for i_in in founded_data[i_data]:
                            
                            if ss_data in i_in:
                                with requests.Session() as s:
                                    s.headers={"User-Agent":"Mozilla/5.0"}
                                    s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
                                    req = s.get(i_in)
                                    if req.status_code == 404:
                                        print("site:{}  status code:[{}]".format(i_in,req.status_code))
                                    elif req.status_code == 200:
                                        print("site:{}  status code:[{}]".format(i_in,req.status_code))
                                                    
       except KeyboardInterrupt:
           pass

        
