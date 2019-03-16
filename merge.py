﻿'''
作者：pk哥
公众号：Python知识圈
日期：2018/09/10
代码解析详见公众号「Python知识圈」。

'''


# 将多个文本内容合并成一个
# 获取目标文件夹的路径
filedir = 'E:\\CET46\\CET4\\txt'
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(filedir)
# 打开当前目录下的result.txt文件，如果没有则创建
f = open('E:\\CET46\\CET4\\txt\\result4.txt', 'w', encoding='UTF-8')
# 先遍历文件名
for filename in filenames:
    filepath = filedir + '\\' + filename
    # 遍历单个文件，读取行数
    for line in open(filepath, encoding='UTF-8'):
        f.writelines(line)
    f.write('\n')
# 关闭文件
f.close()

