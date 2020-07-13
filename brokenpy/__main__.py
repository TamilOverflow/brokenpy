import sys

from brokenpy import *

socilaData = []
target_valid_data = []
global output_filename 
broken = BrokenLinkPy()

def social_link(envpath):
    try:
        with open(envpath+'sociallinks.ini' ,'r') as sslink:
            
            for data in sslink:
                v_data = data.strip()
                #print(v_data)
                socilaData.append(v_data)
    
    except FileNotFoundError as identifier:
        print("File not found {}".format(identifier))

def target_link(envpath):
    print("[+]==================== [Target URL's] ======================== ")
    try:
        with open(envpath+'targetlist.ini' ,'r') as sslink:
            
            for data in sslink:
                v_data = "https://www.{}/".format(data.strip())
                print(v_data)
                target_valid_data.append(v_data)
    
    except FileNotFoundError as identifier:
        print("File not found {}".format(identifier))

def main():
    print("[+] Requirement searching . \n \n")
    envpath ='./'
    social_link(envpath)
    target_link(envpath)

    broken.crawl_req(target_valid_data,socilaData)


    

    

if __name__ == "__main__":
    main()
