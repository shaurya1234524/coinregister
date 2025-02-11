from django.shortcuts import render, HttpResponse
from home.models import Coin
from django.db.models import Q
# def basereturn(request):
#    return render(request,"index.html")
# # Create your views here.
def forms(request):
 return render(request,"forms.html") 


def uploadCoin(request):
  if request.method=="POST":
    name=request.POST.get("name")
    image=request.FILES.get("image")
    description=request.POST.get("description")
    url=request.POST.get("trade_url")
    formsubmit=Coin(name =name,image=image,description=description,url=url)
    formsubmit.save()
  return HttpResponse("form submitted successfully")

def displayall(request):
  displaythings=Coin.objects.all()
  print(displaythings)
  context={'displaythings': displaythings}
  return render(request,'index.html',context)
def searching(request):
  if request.method=="GET":
    query=request.GET.get("querysearch")
    displaythings=Coin.objects.filter(Q(name__icontains=query)|Q(description__icontains=query))
   
    context={'displaythings': displaythings}
    return render(request,'index.html',context)
  