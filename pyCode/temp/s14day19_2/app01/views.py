from django.shortcuts import render, HttpResponse


# Create your views here.


user_dict = {
    '1': {'name': 'jack1', 'age': '12'},
    '2': {'name': 'jack2', 'age': '12'},
    '3': {'name': 'jack3', 'age': '12'},
    '4': {'name': 'jack4', 'age': '12'},
}


def detail(request,page):
    return HttpResponse(page)


def index(request):
    return render(request, 'index.html', {'user_dict': user_dict})

#
# def detail(request, *args):
#     nid = request.GET.get('nid')
#     detail_info = user_dict[nid]
#     return render(request, 'detail.html', {'detail_info': detail_info})
