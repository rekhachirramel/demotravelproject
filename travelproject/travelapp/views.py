from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Person

# Create your views here.
def demo1(request):
   obj=Place.objects.all()

   return render(request,"index.html",{'result1':obj})
def demo(request):
   obj1=Person.objects.all()
   return render(request,"index.html",{'result':obj1})

#def about(request):
  # return render(request,"about.html")
#def contact(request):
   #return HttpResponse("hello iam contact")