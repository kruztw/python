from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

title_tag = soup.title
print(title_tag)

print(title_tag.string)


a_tags = soup.find_all('a')
for tag in a_tags:
    print(tag.string)
    print(tag.get('href'))


# 搜尋所有超連結與粗體字
tags = soup.find_all(["a", "b"])
print(tags)


# 限制搜尋結果數量
tags = soup.find_all(["a", "b"], limit=2)
print(tags)


# 預設會以遞迴搜尋
soup.html.find_all("title")


# 不使用遞迴搜尋，僅尋找次一層的子節點
soup.html.find_all("title", recursive=False)

