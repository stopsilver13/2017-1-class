from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(request) :
    return render(request, 'blog/post_list.html')

def post_detail(request, id) :
    return HttpResponse('{}번 글을 보자.'.format(id))