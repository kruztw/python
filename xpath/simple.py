from lxml import etree

html_doc ="""
<html>
    <head></head>
    <body>
        <li>
            <a href="a_href" title="a_title">
                <img src="/16860s.jpg">
            </a>
        </li>
        <li id="li_id">
            <div>
                <p> hello </p>
                <p> world </p>
            </div>
        </li>

    </body>
</html>"""


page = etree.HTML(html_doc)
print(page.xpath('string(/html/body/li[2]/div/p)')) #  / : 一層一層找
print(page.xpath('string(//p)'))                    # // : 全體一次找
print(page.xpath('string(//p[1])'))                 # 從 1 開始
print(page.xpath('string(//p[2])'))                 # 從 1 開始
print(page.xpath('//li[2]/div/p/text()'))           # 除了 string 外, 也可以用 text() 獲取字串

print(page.xpath('//p/..'))                         # div


print(page.xpath('//li')[1].xpath('@id'))           # 這種寫法 index 從 0 開始, @ 獲取屬性
print(page.xpath('//li')[1].xpath('@id="li_id"'))   # 這裡一個 = 是比較, 不是 asign
print(page.xpath('//a[@href="a_href"]'))            # 找尋 href == "a_href" 的 a

