from selenium import webdriver
import os
import requests
import shutil

searchterm = 'cat'
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser = webdriver.Chrome()
browser.get(url)
img_count = 0
extensions = { "jpg", "jpeg", "png", "gif" }
if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(20000):
    browser.execute_script("window.scrollBy(0,10000)")
    
html = browser.page_source.split('["')
imges = []
for i in html:
    if i.startswith('http') and i.split('"')[0].split('.')[-1] in extensions:
        imges.append(i.split('"')[0])

for img in imges:
        img_count += 1
        img_url = img
        img_type = img.split('.')[-1]
        filename =  searchterm + "_" + str(img_count) + "." + img_type
        filepath = "E:\\scrape_data\\ok\\" + filename

        resp = requests.get(img_url, stream=True)
        try:
            local_file = open(filepath, 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            del resp
            print("save (" + str(img_count) + ") ok")
        except:
            print("save error")

browser.close()