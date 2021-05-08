from django.shortcuts import render
from django.http import HttpResponse

    # Create your views here.
def index(request):
        #my_dict={'insert_me':"hello i m from views.py i m in tempapp in templates"}
        return HttpResponse("<em>hello world this is help page</em>")
        #return render(request,'tempapp/temp.html',context=my_dict)
def help(request):
        help_dict={'help_insert':'help page'}
        return render(request,'tempapp/temp.html',context=helpdict)
