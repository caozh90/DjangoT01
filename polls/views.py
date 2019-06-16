# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # 测试程序
    return HttpResponse("Hello, World. Your are at the polls index.")

def detail(request,qustion_id):
    return  HttpResponse('You are looking at question %s.' %qustion_id)

def results(request, qustion_id):
    response = "You're looking at the results of question %s."
    return  HttpResponse(response %qustion_id)

def vote(request,qustion_id):
    return HttpResponse("You're voting on question %s." %qustion_id)