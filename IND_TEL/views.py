from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyderabad(request):
    places=["Golkonda","sanghi","charminar","chilkur","Ramoji Film City"
        
    ]
    context={"places":places}

    return render(request,'hyd.html',context)

def warangal(request):
    response="<h1>welcome to warangal</h1>"
    return HttpResponse(response)

