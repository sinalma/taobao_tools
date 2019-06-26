import csv
import pandas as pd

with open('C:/Users/sinalma/Desktop/20181214_all_01.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    column1 = [row[1]for row in reader]
    print(column1)


# 下面是按照列属性读取的
d = pd.read_csv('C:/Users/sinalma/Desktop/20181214_all_01.csv','rb', usecols=['case', 'roi', 'eq. diam.','x loc.','y loc.','slice no.'])
print(d)

d = pd.read_csv('C:/Users/sinalma/Desktop/20181214_all_01.csv','rb', usecols=['case', 'roi', 'eq. diam.','x loc.','y loc.','slice no.'],
                nrows=10)
# 这是表示读取前10行
 