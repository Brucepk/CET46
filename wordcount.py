import re
import os

'''
作者：pk哥
公众号：Python知识圈
日期：2018/09/10
代码解析详见公众号「Python知识圈」。

'''


def WordList(file):
    with open(file, encoding='UTF-8') as f:
        text = f.read()
        return text.split()


def save2txt(path, data):
    print('正在保存信息')
    with open(path + 'count.txt', 'a', encoding='utf-8')as f:
        for i in data:
            f.write(str(i))
            f.write('\n')
        print('保存成功！')


file = 'E:\\CET46\\CET6\\txt\\result6.txt'
result = WordList(file)
words = [i.lower() for i in re.findall('[a-zA-Z]+', str(result)) if len(i) > 2]
d = dict()
common_word = ['the', 'and', 'for', 'are', 'that', 'you', 'not', 'one', 'this', 'people']
for word in words:
    if word not in common_word:
        d[word] = d.get(word, 0) + 1    # 获取 key 的值，默认为 0
        data = sorted(d.items(), key=lambda x: x[1], reverse=True)
path = 'E:\\CET46\\CET6\\txt\\'
save2txt(path, data)




