import numpy
a = numpy.array([2, 0, 1, 5, 8, 3])
print('最大值',a.max())
print('最小值',a.min())
a.sort()
print('排序',a)
print(a[0:2])
print(a[2])
print(a[-2])