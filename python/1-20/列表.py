items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# 切片
print(items8[0:2])
print(items8[0:5:1])
print(items8[0:4:2])
print(items8[-1:-5:-2])

# 列表可变
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
languages.insert(1, 'SQL')
print(languages)
if "c++" in languages:
    languages.remove('c++')
print(languages)
languages.pop(2)
print(languages)
# languages.clear()
# print(languages)

"""列表的sort操作可以实现列表元素的排序，reverse操作可以实现元素的反转"""
