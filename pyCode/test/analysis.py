#coding=utf-8
# 读取数据 header设置Excel无标题头
import pandas as pd

data = pd.read_excel("missing_data.xls", header=None)
print('读取源数据\n',data)

# 计算数据长度
print('文本总行数\n', len(data))
# 计算用户A\B\C用电总和
print('计算用户A\B\C用电总和\n',data.sum())

# 计算用户A\B\C用电量算术平均数
mm = data.mean()
print('计算用户A\B\C用电量算术平均数\n',mm)

# 输出预览前5行数据
print('预览前5行数据\n',data.head(5))

# 输出数据基本统计量
print('输出数据基本统计量\n',data.describe())



import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='SimHei', size=20)

num = np.array([13325, 9403, 9227, 8651])
ratio = np.array([0.75, 0.76, 0.72, 0.75])
men = num * ratio
women = num * (1 - ratio)
x = [u'聊天', u'支付', u'团购\n优惠券', u'在线视频']

width = 0.5
idx = np.arange(len(x))
plt.bar(idx, men, width, color='red', label=u'男性用户')
plt.bar(idx, women, width, bottom=men, color='yellow', label=u'女性用户')
plt.xlabel(u'应用类别')
plt.ylabel(u'男女分布')
plt.xticks(idx + width / 2, x, rotation=40)
plt.legend()
plt.show()
############################################################
import matplotlib.pyplot as plt
fracs = [45, 30, 25]  # 每一块占得比例，总和为100
n = mm[0] + mm[1] + mm[2]
a = (mm[0] * 1.0 * 100 / n)
b = (mm[1] * 1.0 * 100 / n)
c = (mm[2] * 1.0 * 100 / n)
print(a, b, c, n)
fracs = [a, b, c]
explode = (0, 0, 0.08)  # 离开整体的距离，看效果
labels = 'A', 'B', 'C'  # 对应每一块的标志
plt.pie(fracs, explode=explode, labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=90, colors=("g", "r", "y"))
# startangle是开始的角度，默认为0，从这里开始按逆时针方向依次展开
plt.title('Raining Hogs and Dogs')  # 标题
plt.show()