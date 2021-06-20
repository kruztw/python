# https://docs.python.org/3/howto/regex.html

import re

p = re.compile('ab*', re.IGNORECASE)
m1 = p.match("abcd")
m2 = p.match("123abcd")

print(m1.start(), m1.end(), m1.span())
print(m2)

m3 = p.search("123abcd")
print(m3.span())

m = re.match("([ab])+", "abcd")
print(m.span())

p = re.compile(r'\d+')
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
for match in iterator:
    print(match.span())



p = re.compile('l(l(lv2)v1)v0')
m = p.match('lllv2v1v0')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(0, 1, 2), m.groups())  # groups 從 1 開始


# sub => substitute
p = re.compile('(blue|white|red)')
print(p.subn('colour', 'blue socks and red shoes'))
print(p.subn('colour', 'no colours at all'))

