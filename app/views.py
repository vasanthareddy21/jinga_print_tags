from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'name':'VASU','age':23}
    return render(request,'data_render.html',context=d)
    
def conditions(request):
    d={'a':100,'b':600,'c':300}
    return render(request,'conditions.html',context=d)