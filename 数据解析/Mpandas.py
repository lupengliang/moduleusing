import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# 1. Series的创建
# 1.1 使用列表创建Series 默认索引为0到N-1的整数型索引
print(Series(data=[1, 2, 3, 4, 5]))

# 1.2 使用numpy数组创建Series
print(Series(data=np.random.randint(0, 100, size=(10,))))

# 1.3 还可以通过设置index参数指定索引 为开闭区间；整数为索引默认为半开区间
s = Series(data=[1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])  # 显示索引
print(s[1])  # 隐式索引
print(s['b'])  # 显示索引
print(s[0:2])  # 隐式切片
print(s['a':'b'])  # 显示切片
print(s.head(3))  # 查看前3个
print(s.tail(3))  # 查看后3个

# 1.4 去重
s = Series([1, 2, 3, 1, 4, 55, 5, 2])
print(s.unique())

# 1.5 相加两个Series
s1 = Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = Series([1, 2, 3], index=['a', 'd', 'c'])
s = s1 + s2
print(s)  # NaN 表示空

# 1.6 检测数据是否为空值
print(s.isnull())
print(s.notnull())
print(s[[1, 2]])  # 取出两个值
print(s[['b', 'c']])  # 取出两个值
print(s[[True, False, True, False]])  # 打印有值的，省略空值
print(s[s.notnull()])  # 打印有值的，省略空值


# 2. DataFrame == mysql的table
# 2.1 使用ndarray创建DataFrame
df = DataFrame(data=np.random.randint(0, 100, size=(3, 4)), index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
print(df.values)  # 所有值
print(df.columns)  # 列索引
print(df.index)  # 行索引
print(df.shape)  # 形状 3行4列


# 2.2 使用字典创建DataFrame key为列索引，value为值，行索引要指定index
dic = {
    '张三': [150, 150, 150, 150],
    '李四': [0, 0, 0, 0]
}
df = DataFrame(data=dic, index=['语文', '数学', '英语', '理综'])
print(df)

# 2.3 获取列索引数据
print(df['张三'])  # 获取张三的成绩

# 2.4 获取前两列
print(df[['张三', '李四']])

# 2.5 获取行索引数据
print(df.loc['语文'])
print(df.iloc[0])

print(df['张三']['英语'])
print(df.loc['英语', '张三'])
print(df.loc[['数学', '英语'], '张三'])
print(df.iloc[:, 0:1])  # 获取第1列 张三列
print(df.iloc[0:1])  # 获取语文行


