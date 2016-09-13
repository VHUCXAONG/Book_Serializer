import urllib
import urllib2
import re

def transfer(num):
    number_dic = {0:"零", 1:"一",2:"二" ,3:"三" ,4:"四" ,5:"五" ,6:"六" ,7:"七" ,8:"八" ,9:"九"}
    i = 1;
    number_list = []
    while (num > 9):
        tail = num % 10
        num /= 10
        i = i + 1
        number_list.append(tail)
    number_list.append(num)

    str_len = len(number_list)
    num_str = number_dic[number_list[str_len - 1]]

    if str_len == 2:
        num_str += "十"
        if number_list[0] != 0:
            num_str += number_dic[number_list[0]]

    if str_len == 3:
        num_str += "百"
        if number_list[1] > 0 or number_list[0] > 0:
            num_str = num_str + number_dic[number_list[1]] + "十"
        if number_list[0] > 0:
            num_str += number_dic[number_list[0]]
    return num_str


class Crawler:
    def __init__(self, book):
        self.chapter_number = book.chapter_number
        self.source_url = book.source_url
        self.page_url_rule = book.page_url_rule
        self.content_url_rule = book.content_url_rule

    def get_page(self):
    try:
        request = urllib2.Request(self.source_url.encode("utf-8"))
        print url
        response = urllib2.urlopen(request)
        return response.read()
    except urllib2.URLError, e:
        if hasattr(e,"reason"):
            print u"连接失败",e.reason
            return None

    def get_content_url(self):
        chapter_url = []
        page = self.get_page()
        pattern = re.compile(page_url_rule)
        result = re.findall(pattern, page)
        for r in result:
            if r[1] != location:
                chapter_url.append(r[0])
            else:
                chapter_url.append(r[0])
                break
        return chapter_url

    def get_content(self):
        all_url = self.get_content_url()
        content = []
        for u in all_url:
            page = self.get_page(u)
            pattern = re.compile(self.content_url_rule)
            result = re.findall(pattern, page)
            content.append(result[0])
        return content
