"""a操作(在原来内容的尾部追加新的内容)，w操作（截断之前的文本内容写入新的内容），"""
# file=open('a.txt','r', encoding='utf8')
# print(file.read())
# file.close()

file = open('致橡树.txt', 'a', encoding='utf-8')
file.write('\n标题：《致橡树。。》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.write("cgx")
file.close()