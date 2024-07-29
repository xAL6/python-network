

# r=requests.get("https://www.woniuxy.com")

# # 解析網頁所有連結
# links=re.findall('<a href="(.*?)"',r.text)
#     # 根據頁面特性排除不要的內容
# for link in links:
#     if link.startswith('#'):
#         continue

#     if link.startswith('/'):
#         link="https://www.woniuxy.com"+link

#     print(link)

#     # 將頁面保存在本地
#     r=requests.get(link)
#     with open('/woniu/page/'+link.split('/')[-1]+time.strftime("_%Y%m%d_%H%M%S",time.localtime())+".html","w",encoding="utf-8") as f:
#         f.write(r.text)

    
# 爬取首頁圖片
import re,requests
def get_image(url):
    r=requests.get(url)
    images=re.findall('<img src="(.*?)"',r.text)
    for image in images:
        if image.startswith('@') or not image:
            continue

        print(image)
        if image.startswith('/'):
            image=url+image
        image_page=requests.get(image)
        with open('./woniu/image/'+image.split("/")[-1],'wb') as f:
            f.write(image_page.content)

get_image("https://www.woniuxy.com")


