from bs4 import BeautifulSoup
import requests


# 查找頁面元素
# print(html.head.title.string)  # 獲取頁面標題文本內容
# print(html.div) # 查找第一個div
# print(html.div.div.div)
# 查找頁面元素通用的方法
# # 1.find_all:根據標籤、屬性,等進行查找
# # 2.select: css selector,div #id,.class

# # 查找頁面所有超連結
# links=html.find_all('a')
# for a in links:
#     if 'href' in a.attrs:
#         print(a['href'])

# # 查找所有圖片
# images=html.find_all('img')
# for image in images:
#     if 'src' in image.attrs:
#         print(image['src'])

# # 查找特定id
# # keyword=html.find(id='keyword')
# # print(keyword['placeholder'])

# # 查找特定class
# titles=html.find_all(class_='news-content-title')
# for title in titles:
#     print(title.string)

title=html.find(text='')
print(title.parent)
print(title.parent.parent)

# 以xpath風格查找 //div[@class='title']
titles=html.find_all('div',{'class':'title'})
for title in titles:
    print(title.string)




def crawl_images(url):
    r=requests.get(url)

    # 初始化解析器
    html=BeautifulSoup(r.text,'lxml')
    ul=html.find('ul',class_='movieList')
    li_tags=ul.find_all('li')

    for li in li_tags:
        movie_name=li.find('img')['title']
        # a=li.find('a')['href']
        # r=requests.get(url+a)
        # with open('./movie/'+movie_name+'.html','w',encoding='utf-8') as file:
        #file.write(r.text)
        img=li.find('img')['src']

        r=requests.get('/'.join(url.split('/')[0:-2])+'/'+img)
 
        with open('./image/'+movie_name+'.jpg','wb') as file:
            file.write(r.content)

if name == "__main__":
    url='https://www.vscinemas.com.tw/vsweb/film/coming.aspx/'
    crawl_images(url)




