# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # 测试程序
    return HttpResponse("Hello, World. Your are at the polls index.")
