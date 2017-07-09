#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__author__ = "Colby"
import sys,os
pt1=os.path.dirname(os.path.abspath(__file__))
print('pt1',pt1)
sys.path.append(pt1)
pt2=os.path.dirname(os.path.abspath(__file__))
print('pt2',pt2)

from  module import moduleTest
moduleTest.say_hello()
print('')

