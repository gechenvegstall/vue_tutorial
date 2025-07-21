import csv
import random

# with open('a.csv', 'w',encoding='utf8',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['姓名', '语文', '数学', '英语'])
#     names = ['a', 'b', 'c', 'a1', 'a2']
#     for name in names:
#         scores = [random.randrange(10, 101) for _ in range(3)]
#         scores.insert(0, name)
#         writer.writerow(scores)


with open('a.csv', 'r',encoding='utf8',newline='') as file:
    reader = csv.reader(file, delimiter='|')
    for data_list in reader:
        print(reader.line_num, end='\t')
        for elem in data_list:
            print(elem, end='\t')
        print()