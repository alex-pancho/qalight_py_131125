import requests
from lxml import html

resp = requests.get("https://lxml.de/")
print(resp)
# print(resp.text)
tree = html.fromstring(resp.text)

title = tree.findtext('.//title')
print("Заголовок сторінки:", title)

eyecatcher = tree.findtext('.//*[@class="eyecatcher"]')
print(eyecatcher)

eyecatcher = tree.xpath('//*[@class="eyecatcher"]')
print(eyecatcher[0].text)

links = tree.xpath('//a/@href')
for link in links:
    print("Посилання:", link)

title = tree.xpath('//title/text()')[0]
print("Заголовок сторінки:", title)


css_selector_1 = "div#introduction.section>p>a.reference.external"
xpath = '//*[@id="introduction"]/p/a[@class="reference external"]'

links = tree.cssselect(css_selector_1)

for a in links:
    print(a.text, a.get("href"))

""