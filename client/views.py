from django.shortcuts import render
from client.forms import addform
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from client.models import Clientinfo
# Create your views here.
def home(request):
    return render(request,'home.html')



def add_Client(request):
        form=addform()
        return render(request,'addclient.html',{'acd':form})


@csrf_exempt
def submit(request):
    form=addform(request.POST)
    form.save()
    return HttpResponseRedirect('/home/')

def view_client(request):
    name=Clientinfo.objects.all()
    return render(request,'viewclients.html',{'list':name})   

def client_detail(request):
    name1=Clientinfo.objects.filter(name=request.GET['name']).all().values()
    return render(request,'list.html',{'list1':name1})


