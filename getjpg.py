from urllib import request


def getHtml(url):
    response = request.urlopen(url)
    html = response.read()
    return html


url = "https://baike.baidu.com/item/%E4%BD%A0%E5" + \
    "%A5%BD%E5%95%8A%EF%BC%8C%E8%87%AA%E5%B7%B1/18839845?fr=aladdin"
html = getHtml(url)
print(html)
with open("test.html", mode="wb") as f:
    f.write(html)
