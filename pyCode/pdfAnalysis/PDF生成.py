#!/usr/bin/env python2.6
#coding:utf-8
import traceback

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.pdfbase import pdfmetrics, ttfonts

#注意data的类型，
#每一个数据点是一个元组
#一条曲线对应一个存储数据点元组的元组
#一个图形可以包含多条曲线，用列表存储曲线元组
data=[((1,100),(2,200),(3,300),(4,400),(5,500)),((1,50),(2,80),(3,400),(4,40),(5,70))]

drawing = Drawing(500, 300)

lp = LinePlot()
lp.x = 50 #坐标轴中心坐标
lp.y = 30
lp.height = 250
lp.width = 400
lp.data = data
lp.joinedLines = 1
lp.lines.symbol = makeMarker('FilledCircle')

lp.xValueAxis.valueMin = 1
lp.xValueAxis.valueMax = 5
lp.xValueAxis.valueStep = 1

lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 500
lp.yValueAxis.valueStep = 100
drawing.add(lp)

title = Label()
#若需要显示中文，需要先注册一个中文字体
pdfmetrics.registerFont(ttfonts.TTFont("haha", "simsun.ttc"))
title.fontName   = "haha"
title.fontSize   = 12
title_text = '你好'
#title_text = "abc"
title._text = title_text
title.x          = 250
title.y          = 280
title.textAnchor ='middle'
drawing.add(title)

Xlabel = Label()
Xlabel._text = 'x'
Xlabel.fontSize   = 12
Xlabel.x          = 480
Xlabel.y          = 30
Xlabel.textAnchor ='middle'
drawing.add(Xlabel)

Ylabel = Label()
Ylabel._text = "y"
Ylabel.fontSize   = 12
Ylabel.x          = 40
Ylabel.y          = 295
Ylabel.textAnchor ='middle'
drawing.add(Ylabel)

try:
     drawing.save(formats=['gif'],outDir=".",fnRoot="abc")
except:
     traceback.print_exc()