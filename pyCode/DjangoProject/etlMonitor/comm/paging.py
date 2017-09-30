# coding=utf-8
# Version:python3.5.2
# Tools:Pycharm
# Date:
from django.utils.safestring import mark_safe

__author__ = "Colby"

class Page(object):
    def __init__(self, currentPage, totalCount, perSize=10, pageCodeNum=10):
        '''
        分页功能的实现：通过传入当前页、总记录数、以及每页记录数，
        返回页码标签栏
        :param currentPage: 当前页，通过client传入
        :param totalCount: 总记录数，调用后台查询，获取记录总数
        :param perSize: 每页显示记录数由前端传入，默认10条,传入偶数
        :param pageCodeNum: 页码显示个数，默认是10+1,这个值一般不变化
        '''
        self.currentPage = currentPage
        self.totalCount = totalCount
        self.perSize = perSize
        self.pageCodeNum = pageCodeNum

    @property
    def beginCount(self):
        return (self.currentPage - 1) * self.perSize

    @property
    def endCount(self):
        return self.currentPage * self.perSize

    @property
    def totalPage(self):
        totalPage, yushu = divmod(self.totalCount, self.perSize)
        if yushu:
            totalPage += 1
        return totalPage

    def pageStr(self, base_url):
        if self.totalPage < self.pageCodeNum:
            firstPage = 1
            lastPage = self.totalPage
        else:
            if self.currentPage <= (self.pageCodeNum + 1) / 2:
                firstPage = 1
                lastPage = self.pageCodeNum + 1
            elif self.currentPage >= self.totalPage - (self.pageCodeNum - 1) / 2:
                firstPage = self.totalPage - self.pageCodeNum
                lastPage = self.totalPage
            else:
                firstPage = self.currentPage - (self.pageCodeNum - 1) / 2
                lastPage = self.currentPage + (self.pageCodeNum + 1) / 2
        pageStr = []
        selectPageSize="""
        
        """
        tempStr = '<li><a href="%s?page=%s">首页</a></li>' % (base_url, 1)
        pageStr.append(tempStr)

        if self.currentPage == 1:
            tempStr = '<li><a href="javascript:void(0);">上一页</a></li>'
        else:
            tempStr = '<li><a href="%s?page=%s">上一页</a></li>' % (base_url, self.currentPage - 1)
        pageStr.append(tempStr)
        for j in range(int(firstPage), int(lastPage) + 1):
            if j == self.currentPage:
                tempStr = '<li><a class="activePage" href="%s?page=%s">%s</a></li>' % (base_url, j, j)
            else:
                tempStr = '<li><a href="%s?page=%s">%s</a></li>' % (base_url, j, j)
            pageStr.append(tempStr)

        if self.currentPage == self.totalPage:
            tempStr = '<li><a href="javascript:void(0);">下一页</a></li>'
        else:
            tempStr = '<li><a href="%s?page=%s">上一页</a></li>' % (base_url, self.currentPage + 1)
        pageStr.append(tempStr)

        tempStr = '<li><a href="%s/?page=%s">尾页</a></li>' % (base_url, self.totalPage)
        pageStr.append(tempStr)
        jump = """
                <input type='text' class="jumpToPage"/><a onclick='jumpTo(this, "%s?page=");'>GO</a>
                <script>
                function jumpTo(ths,base){
                    var val = ths.previousSibling.value;
                    if (val==undefined || val=="" || val==null){
                        alert("Go页码不能为空");
                    }else {
                        if (!isNaN(val)){
                        location.href = base + val;
                        }else{
                        }
                    }
                }
        </script>
                """ % (base_url,)
        pageStr.append(jump)
        pageStr = ''.join(pageStr)
        pageStr = mark_safe(pageStr)
        return pageStr
