from django.utils.safestring import mark_safe

class PageInfo:
    """
    传入当前页、记录总数，每页显示记录数
    返回开始页、结束页、总页数
    """
    def __init__(self,current_page,all_count,per_item=20):
        self.CurrentPage=current_page
        self.AllCount = all_count
        self.PerItem = per_item
    @property
    def start(self):
        return (self.CurrentPage - 1) * self.PerItem

    @property
    def end(self):
        return self.CurrentPage*self.PerItem

    @property
    def all_page_count(self):
        #余数、商
        temp = divmod(self.AllCount, self.PerItem)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        return  all_page_count

def pager(page,count):
    """
    传入当前页和记录总数，返回首页、尾页、上一页、下一页，
    （一个字符串），且显示前5页后5页
    """
    page_html = []
    first_page = "<a href='/index/%d'>首页</a>" % (1)
    page_html.append(first_page)
    if page <= 1:
        prv_html = "<a href='#'>上一页</a>"
    else:
        prv_html = "<a href='/index/%d'>上一页</a>" % (page - 1)
    page_html.append(prv_html)
    # 当前页在中间，显示前五页和后五页
    if count < 11:
        begin = 1
        end = count
    else:
        if page < 6:
            begin = 0
            end = 11
        else:
            if page + 6 > count:
                begin = page - 5
                end = count
            else:
                begin = page - 6
                end = page + 5

    for i in range(begin, end):
        if page == i + 1:
            a_html = "<a style='color:red' href='/index/%d'>%d</a>" % (i + 1, i + 1)
        else:
            a_html = "<a href='/index/%d'>%d</a>" % (i + 1, i + 1)
        page_html.append(a_html)
    next_html = "<a href='/index/%d'>下一页</a>" % (page + 1)
    page_html.append(next_html)
    end_page = "<a href='/index/%d'>尾页</a>" % (count)
    page_html.append(end_page)
    page = mark_safe(''.join(page_html))
    return page
