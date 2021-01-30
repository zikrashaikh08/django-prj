from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world(request):
    params = {'name':'zikra','place':'mumbai'}
    return render(request,'base.html', params)

def index_page(request):
    return render(request,'index.html')
