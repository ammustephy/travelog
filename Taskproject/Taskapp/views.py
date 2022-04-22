from django.http import HttpResponse
from django.shortcuts import render
from . models import Images

# Create your views here.
def demo(request):
    obj=Images.objects.all()
    #name="Page"
    return render(request,"index.html",{'result':obj})
#def calc(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #c=x+y
    #d=x-y
    #e=x*y
    #f=x/y
    #return render(request,'result.html', {'result1':c, 'result2':d, 'result3':e, 'result4':f})
