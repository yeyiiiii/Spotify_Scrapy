from lxml import etree
import requests

# 要爬取的url
url = "https://open.spotify.com/album/2rQub6XmlQJb8bGYHhjBsD?si=5R-p3w3kQ4OyINBV8lgnGw&nd=1"

# 模仿浏览器的headers
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    
}

# 唱片名
# /html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[1]/div[5]/span/h1
# 表演者
# /html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[1]/div[5]/div/div/span/a
# 发行时间
# /html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[2]/div/p
# 出版者
# /html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[2]/div/div/p[2]
# 曲目
# /html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div

# get请求，传入参数，返回结果集
resp = requests.get(url,headers=headers) # <Response [200]>

# 将结果集的文本转化为树的结构
tree = etree.HTML(resp.text)
# result = etree.tostring(tree)
# print(result.decode('UTF-8'))
album_name = tree.xpath("//span[@class='rEN7ncpaUeSGL9z0NGQR']/h1/text()")  # 获取唱片名
print(album_name)
'''
# 定义列表存储所有数据
dli = []
li = []
#根据树的路径找到对应的数据集
album_name = tree.xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[1]/div[5]/span/h1/text()")  # 获取唱片名
artist = tree.xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[1]/div[5]/div/div/span/a/text()") # 获取表演者
release_date = tree.xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[2]/div/p/text()") # 获取发行时间
label = tree.xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[2]/div/div/p[2]/text()") # 获取出版者
track = tree.xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/text()") # 获取曲目
#获取数据集中的元素
li.append(album_name[0])
li.append(artist[0])
li.append(release_date[0])
li.append(label[0])
li.append(track[0])
dli.append(li)

# 打印数据
for dd in dli:
    print(dd)
'''
